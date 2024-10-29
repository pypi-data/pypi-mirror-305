import importlib # for using Agents from package dynamically
import json
from types import ModuleType

from dapu.process import DapuProcess # decorator
from dapu.process import logging
from dapu.jobstatus import JobStatus
from dapu.manager import DapuManager
from dapu.context import DapuContext
from dapu.agents.agent import AgentGeneric

class DapuJob():

    def __init__(self, agenda_id: int, context: DapuContext):
        self.agenda_id: int = agenda_id
        self.context: DapuContext = context
        self.agent_modules_loaded: dict = {} # to avoid double load of module
        # NEXT ones will be loaded from database using agenda_id
        self.task_id: str = '' 
        self.actions: list[dict] = []
        self.priority: int = 6 # let default be something bigger
        self.route_alias: str | None = None 
        self.route_type: str | None = None
        self.route_code: str | None = None
        # 
        self.start_str_iso_ts: str = None # TS as ISO formatted string
        if not self.load_agenda_details(): # uses self.agenda_id
            raise Exception("Bad initialization of job")
    

    def load_agenda_details(self) -> bool: # runs at end of INIT
        agenda: str = self.context.find_registry_table_full_name('agenda')
        route: str = self.context.find_registry_table_full_name('route')
        registry: str = self.context.find_registry_table_full_name('registry')
        
        # safe sql (InS 2024-08-26): agenda_id is garanteed always as py int 
        sql = f"""SELECT a.task_id
                , r.actions as actions
                , a.priority -- for giving priority +1 to dependants
                , rt.alias as route_alias 
                , coalesce(rt.type, 'sql') as route_type
                , rt.code as route_code
            FROM {agenda} a
            JOIN {registry} r ON r.task_id = a.task_id 
            JOIN {route} rt ON split_part(a.task_id, '.', 1) = rt.code AND rt.disabled not ilike '%worker%'
            WHERE a.id = {self.agenda_id} """
        
        result_set = self.context.target(sql)
        if result_set:
            (self.task_id, actions_str, self.priority, self.route_alias, self.route_type, self.route_code) = result_set[0]
            self.actions = json.loads(actions_str)
            return True
        else:
            logging.error(f"No job with agenda_id {self.agenda_id} amoungst enabled for worker routes. Ignore if not repeats.")
            return False


    def run(self) -> bool:
        """
        Entry point: do some logging and housekeeping before and after main point
        and inside execute all actions from task definition for that job
        """
        logging.debug(f"Working directory is {self.context.work_dir}")
        self.mark_job_start() # started marker and database loging
        try:
            was_success = self.task_actions_execute() # MAIN POINT FOR ALL
        except Exception as e1:
            was_success = False
            logging.error(f"{e1}")
        self.mark_job_end(was_success) # mark end of job before finding dependant tasks - updates 3 tables

        if was_success:
            self.dependents_to_agenda() # find depending tasks and put them info agenda
            logging.info(f"{self.task_id} succeeded (job={self.agenda_id})")
        return was_success
    
    
    def dependents_to_agenda(self) -> None:
        """
        Using DapuManager for finding dependant tasks and puting them to agenda for next workers
        Manager will be initialized using current context object
        """
        logging.info(f"Managers sidequest has started")
        dm = DapuManager(self.context)
        dm.add_dependent_tasks_to_agenda(self.task_id, self.priority + 1)
        logging.info(f"Managers sidequest has ended")
        
        
    def prepare_agent(self, command: str, action: dict) -> AgentGeneric | None:
        """
        Returns object of type Agent
        """
        module_name: str = self.find_module_from_action(command) # filename part: agent_runsql
        if module_name is None:
            logging.error(f"Module for command {command} is unclear")
            return None
        logging.debug(f"Module name for {command} is {module_name}")
        agent_module: ModuleType = self.prepare_agent_module(module_name)
        if agent_module is None:
            return None
        return agent_module.Agent(self.task_id, action, self.context, self.route_alias)


    def find_module_from_action(self, action_alias: str) -> str:
        """
        Action code must reside in folder dapu/agents in file agent_<alias>
        Hereby we add prefix "agent_" to alias 
        LATER put here (better mapper) mechanism for Agent-type plugins
        """
        return '_'.join(['agent', action_alias]) #self.implemented_drivers[named_driver][0]
    

    def prepare_agent_module(self, module_name: str) -> ModuleType | None:
        """
        Imports module where agent resides if not already loaded
        Returns module
        """
        if module_name in self.agent_modules_loaded:
            return self.agent_modules_loaded[module_name]
        
        long_module_name: str = '.'.join([self.context.package_name, 'agents', module_name]) # need on built-in moodulid! aga custom?
        try: # lets try to import module, starting from root package and long_module_name
            """ Read https://docs.python.org/3/library/importlib.html """
            agent_module: ModuleType = importlib.import_module(long_module_name, package=self.context.package_name)
            self.agent_modules_loaded[module_name] = agent_module # register found module into dict for reuse
        except Exception as e1:
            msg = f"Cannot import module {long_module_name}"
            logging.error(msg)
            return None
        return agent_module
    
    
    def get_database_time(self, precise_time: bool=True) -> str | None:
        """
        Time in target database as ISO string
        """
        if precise_time:
            sql = "SELECT clock_timestamp()" # Very current time (inside transaction)
        else:
            sql = "SELECT current_timestamp" # Transaction beginning time
        result_set = self.context.target(sql)
        if result_set:
            return result_set[0][0] # ISO string
        return None
    
    
    def task_actions_execute(self) -> bool:
        """
        Job run = execute all actions defined in Task, until first error
        """
        for pos, action in enumerate(self.actions, start=1):
            command: str = action.get('do', None)
            if command is None:
                logging.warning(f"Action step number {pos} is without command, skiping")
                continue
            
            logging.debug(f"Action step number {pos} is {command}")
            agent: AgentGeneric = self.prepare_agent(command, action)
            if agent is None:
                logging.error(f"Cannot work with {command}")
                return False
            
            try:
                step_was_success = agent.do_action() # MAIN POINT FOR ONE ACTION
            except Exception as e1:
                logging.error(str(e1))
                return False
                
            if not step_was_success: # AND action.get('fatal', True) <- idea of extension
                logging.error(f"Step number {pos} {command} failed")
                return False  # first error quits
        # next action for job
        return True # if no failure (incl "no steps no failure")


    @DapuProcess.task_id_eventlog(flag='START') # returns int
    def mark_job_start(self) -> list[tuple]:
        """
        Mark job in Agenda as started, use update/returning and decorator does rest
        """
        self.start_str_iso_ts: str = self.get_database_time(True)
        agenda: str = self.context.find_registry_table_full_name('agenda')
        
        sql: str = f"""UPDATE {agenda} 
            SET status = {JobStatus.BUSY.value}
            , worker = {self.context.worker_id}
            , last_start_ts = clock_timestamp()
            WHERE id = {self.agenda_id}
            RETURNING task_id
            """
        return self.context.target(sql)

    
    def mark_job_end(self, was_success: bool) -> None:
        """
        After job is done (successfully of not) do housekeeping
        End Worker record, mark Agenda ended/failed, refresh jobs Task Registry record
        """
        worker: str = self.context.find_registry_table_full_name('worker')
        registry: str = self.context.find_registry_table_full_name('registry')
        
        add_done: int = 1 if was_success else 0
        add_fail: int = 1 - add_done
        
        # workeri (tegelikult mitte) lõpp (järgmine sama workeri task kirjutab üle)
        sql: str = f"""UPDATE {worker} 
            SET end_ts = current_timestamp
            , count_done = coalesce(count_done, 0) + {add_done} 
            , count_fail = coalesce(count_fail, 0) + {add_fail}
            WHERE id = {self.context.worker_id}"""
        self.context.target(sql, False)
        
        # agendas taski lõpu markeerimine
        if was_success:
            self.save_end()
        else: # kui oli viga, siis tagasi ootele panna (manager tegeleb juba nurjumiste arvuga)
            self.save_error()

        # registris taski viimase jooksu markeerimine
        start_time_literal: str = f"'{self.start_str_iso_ts}'"
        if start_time_literal is None: # 0,001% tõenäosus
             start_time_literal = 'NULL'
        sql: str = f"""UPDATE {registry} 
                SET last_start_ts = {start_time_literal}
                , last_end_ts = clock_timestamp()
            WHERE task_id = '{self.task_id}' """
        self.context.target(sql, False)


    @DapuProcess.task_id_eventlog(flag='END') # returns int
    def save_end(self) -> list[tuple]:
        """
        Mark job in Agenda as ended, use update/returning and decorator does rest
        """
        agenda: str = self.context.find_registry_table_full_name('agenda')
        status: int = JobStatus.DONE.value
        sql: str = f"""UPDATE {agenda} 
            SET status = {status}
            , last_end_ts = clock_timestamp()
            WHERE id = {self.agenda_id}
            RETURNING task_id
            """
        return self.context.target(sql)


    @DapuProcess.task_id_eventlog(flag='ERROR') # returns int
    def save_error(self) -> list[tuple]:
        """
        Mark job in Agenda as failed, increment failure count, use update/returning and decorator does rest
        """
        agenda: str = self.context.find_registry_table_full_name('agenda')
        status: int = JobStatus.IDLE.value
        sql: str = f"""UPDATE {agenda} 
            SET status = {status}
            , last_end_ts = NULL
            , failure_count = failure_count + 1
            WHERE id = {self.agenda_id}
            RETURNING task_id
            """
        return self.context.target(sql)
