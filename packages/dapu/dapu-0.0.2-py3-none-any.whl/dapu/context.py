
from dbpoint.dbpoint import Hub
from typing import Any
#from functools import cache
#from functools import lru_cache

class DapuContext(): # maybe inherit from DapuItem??
    """
    One central class which have one instance what can be 
    given as starting point to all next Dapu-sh components
    (Workers inits Job and Job inits Manager)
    """
    def __init__(self) -> None:
        self.hub: Hub | None = None
        self.list_of_profiles : list[dict]

        # endine hermit klassi osa
        self.work_dir: str | None = None
        #self.target_alias: str | None = None # kassutadea teist!!1
        self.log_level : int = 20 # don't use here enums directly from logging (cycle will occur!)
        self.app_name : str = 'dapu' # for logging and temp dir under system-wide temp dir (don't use spaces, don't live complicated life)
        self.package_name : str = 'dapu' # for dynamic loading
        self.flags: list = []
        self.more_args: list = []

        # endine self osa DapuProcess initist
        self.SQL_CONN_FILE_NAME: str = 'sql.yaml' # in working directori
        self.OPTIONS_FILE_NAME: str = 'options.yaml' # if not existing defaults are used
        # CONSTANTS, lets keep everything same over whole system
        self.PLACEHOLDER_TARGET_SCHEMA: str = '{{target_schema}}'
        self.PLACEHOLDER_TARGET_TABLE: str = '{{target_table}}'
        self.PLACEHOLDER_TARGET_TABLE_SHADOW: str = '{{target_table_shadow}}'
        self.TARGET_ALIAS: str = 'dapu' # main connection name/reference (to database where meta tabels reside)
        
        # Next ones can be overiden (matching some current schema name, or just subjective) by configuration file residing in work_dir (project dir)
        self.DAPU_SCHEMA = 'meta' # the latest idea: lets call schema this way NB! FIXME globalversioning must use placeholders too!!!
        self.DAPU_PREFIX = '' # and lets prefix all tables in above mentioned schema this way
        
        # endine Conf osa:
        # Critical version: myversion vs meta.stopper.allowed_version
        self.MYVERSION = 2 # int, increment it every time when previuos code cannot start any more 
        # All
        self.DAPU_SCHEMA = 'meta' # the latest idea: lets call schema this way 
        self.DAPU_PREFIX = '' # and lets prefix all tables in above mentioned schema this way

        # Cleaner:
        self.DELETE_LOGS_OLDER_THEN: str = "2 months"
        self.DELETE_TRACE_LOGS_OLDER_THEN: str = "15 days"
        self.DELETE_AGENDA_OLDER_THEN: str = "14 months" # PROD keskkonnas soovituslik vähemalt aasta, nt 14 months
        # Registrar:
        self.HAUL_DEF_DIR: str = "defs" # relative, subdir
        self.FILENAME_DEFINITION_FILE: str = 'haulwork.yaml' # NB! väiketäheline!
        self.SUBDIRNAME_VERSION_FILES = 'ver' # for target tables verioning
        self.SUBDIRNAME_DEFINITION_FILES = 'pull'
        self.FILENAME_FOR_DELETION = 'tasks_to_delete.txt'
        # Worker
        # laadimiprotsessi ajaline piiramine (kui see hulk minuteid möödas algusest, siis uut laadimisülesannet ei alusta)
        self.WORKER_NO_NEW_HAUL_AFTER_MINUTES: int = 27
        
        # Enabler
        self.ENABLER_SUB_DIR_NAME = 'ver' # for meta and structure versioning
        self.ENABLER_INDEX_FILE_NAME = 'changes.yaml'
        # Registrar
        self.ROUTE_FILE_NAME = 'route.yaml'
        # Manager
        self.FAILURE_LIMIT : int = 3
        self.DEFAULT_MANAGER_INTERVAL: str = '4 hours'
        self.DEFAULT_KEEP_GOING_INTERVAL: str = '5 hours' # '2 minutes' # '2 days' # valid PG interval, 


        self.worker_id : int = None



#    def __call__(self, *args, **kwargs):
#        return self

#region dbpoint wrappers
    def run(self, *args: list, **kwargs: dict) -> Any:
        return self.hub.run(*args, **kwargs)

    def target(self, *args: list, **kwargs: dict) -> Any:
        return self.hub.run(self.TARGET_ALIAS, *args, **kwargs)
    
    def disconnect_target(self):
        self.hub.disconnect(self.TARGET_ALIAS)

    def disconnect_all(self):
        self.hub.disconnect_all()

    def disconnect_alias(self, profile_name):
        self.hub.disconnect(profile_name)

#endregion

    def full_name_from_root(self, inner_part: str):
        return self.full_name(inner_part)
    
    def full_name_from_pull(self, inner_part: str | list):
        if isinstance(inner_part, str):
            inner_part = [inner_part]
        return self.full_name([self.SUBDIRNAME_DEFINITION_FILES, *inner_part])
    
    def full_name_from_ver(self, inner_part: str):
        return self.full_name([self.ENABLER_SUB_DIR_NAME, inner_part])


    def full_name(self, inner_part: str | list[str]) -> str | None:
        import os
        """
        Returns full name of inside file object (dir or file) short name (or list of part components)
        conn_file_full = os.path.join(self.work_dir, self.SQL_CONN_FILE_NAME)
        """
        if not self.work_dir:
            raise Exception("work_dir dont have value")
        if not inner_part:
            raise Exception("inner part is missing")
        if isinstance(inner_part, str):
            return os.path.join(self.work_dir, inner_part)
        if isinstance(inner_part, list):
            return os.path.join(self.work_dir, *inner_part)
        raise Exception(f"inner part type is wrong {type(inner_part)}")


    #@lru_cache(maxsize=120, typed=False) -> CacheInfo(hits=24, misses=19, maxsize=120, currsize=19) 
    # not very helpful: there are max 7 different arguments (table_short_name), why 19 misses?
    #@cache # now it may have point to use cache (now = after remaking this as context own function)
    def find_registry_table_full_name(self, table_short_name: str) -> str:
        #logging.debug(f"Usage of {table_short_name}")
        """
        from short name makes full table name according to system global setup (compatibility with historical ideas)
        "agenda" -> "meta.bis_agenda" or "bis.agenda" or "bis.bis_agenda"
        """
        schema_part = ''
        if self.DAPU_SCHEMA is not None and self.DAPU_SCHEMA.strip() > '': # if schema name is present
            schema_part = self.DAPU_SCHEMA.strip() + '.' # dot at end as seperator between schema name and table name
        
        table_prefix = ''
        if self.DAPU_PREFIX is not None and self.DAPU_PREFIX.strip() > '':
            table_prefix = self.DAPU_PREFIX.strip()
        
        return ('').join([schema_part, table_prefix, table_short_name])


    def find_loaded_profile(self, profile_name: str) -> dict:
        name_key: str='name'
        profile: dict = {}
        for one_profile in self.list_of_profiles:
            if isinstance(one_profile, dict) and one_profile.get(name_key) == profile_name:
                profile = one_profile.copy()
                break
        return profile


    def replace_compatibility(self, sql: str, local_replacements : list[tuple] = []) -> str:
        """
        Owner is nice trick here (so each new schema can be created with minimal effort (copy-paste))
        """
        replacements = []
        replacements.append(('{schema}', self.DAPU_SCHEMA))
        replacements.append(('{prefix}', self.DAPU_PREFIX))
        replacements.append(('{owner}', self.hub.get_profile(self.TARGET_ALIAS)['username'])) # after schema create
        for local_replacement in local_replacements: # orvuke tegelt (orphan, never assigned yet)
            replacements.append(local_replacement) # tuple[str, str]
        
        for replacement in replacements:
            sql = sql.replace(replacement[0], replacement[1])
        return sql
   