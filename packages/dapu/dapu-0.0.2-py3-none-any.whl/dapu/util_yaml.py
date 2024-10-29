import yaml # python -m pip install pyyaml
import logging # ega see rida siin ei kirjuta üle süstemset?
import os



# enabler uses
def load_yaml(yaml_dir: str|None, yaml_file:str, empty_as:any = []) -> any :
    """
    Two way to point to file: 
    a) dir full path and file name, 
    b) None and file full path
    Return type is usually list or dict and depends on content of file
    """
    if yaml_dir is None:
        full_file_name = yaml_file
    else:
        full_file_name = os.path.join(yaml_dir, yaml_file)
    if not os.path.exists(full_file_name):
        msg = f"File {full_file_name} is not existing (it may be fine)"
        logging.warning(msg)
        return empty_as
    
    try:
        return yaml.load(open(full_file_name, encoding="utf-8"), Loader=yaml.Loader) or empty_as
    
    except Exception as e1:
        logging.error(str(e1))
        logging.error(f"Some error happenes while reading {full_file_name} as YAML")
        return empty_as
