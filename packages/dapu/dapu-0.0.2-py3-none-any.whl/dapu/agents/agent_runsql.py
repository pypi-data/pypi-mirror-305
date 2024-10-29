from dapu.agents.agent import AgentGeneric
from dapu.process import logging
from dapu.perks import split_task_id

class Agent(AgentGeneric):
    
    def do_action(self) -> bool:
        
        file_element = 'file'
        existing_files = self.collect_files(file_element)
        if not existing_files:
            logging.error(f"No files for tag {file_element} in {self.task_dir}")
            return False
    
        _, schema_name, table_name = split_task_id(self.task_id)
        replacements: list[dict] = []
        replacements.append((self.context.PLACEHOLDER_TARGET_SCHEMA, f'{schema_name}'))
        replacements.append((self.context.PLACEHOLDER_TARGET_TABLE, f'{table_name}'))
        
        return self.apply_files_to_target(existing_files, replacements)
    
