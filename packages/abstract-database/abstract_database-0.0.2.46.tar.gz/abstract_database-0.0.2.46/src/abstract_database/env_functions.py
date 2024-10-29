from abstract_security import *
from .connection_manager import*
from abstract_utilities import safe_read_from_json,SingletonMeta
import json,os
def get_abs_path():
    return os.path.abspath(__file__)
def get_abs_dir():
    return os.path.dirname(get_abs_path())
def make_abs_path(path):
    return os.path.join(get_abs_dir(),path)
def get_db_key(dbName,dbType,extra=None):
    key = f"{dbName.upper()}_{dbType.upper()}"
    if extra:
        key+=f"_{extra.upper()}"
    return key
def get_bot_name():
    return 'darnell'
def get_pure_env_value(key=None,path=None):
    return get_env_value(path=path or get_env_path(),key=key)
def get_bot_env_key(key):
    key = f"{get_bot_name()}_{key}"
    return get_env_value(path=get_env_path(),key=key)
def get_env_key(key,path=None):
    return get_pure_env_value(path=path or get_env_path(),key=key)
def get_open_ai_key():
    return get_env_key('open_ai')
def get_discord_token():
    return get_env_key('token')
def get_application_id():
    return get_env_key('application_id')
def get_client_id():
    return get_env_key('client_id')
def get_client_secret():
    return get_env_key('client_secret')
def get_public_key():
    return get_env_key('public_key')
def get_dbType(dbType=None):
    return f"_{dbType}" if dbType else ''
def create_insert_list_file(dbName,dbType=None):
    return f"{dbName}{get_dbType(dbType)}_table_config.json"
class envManager(metaclass=SingletonMeta):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.tables_dir= '/home/shared/auths/tables'
            self.env_path = '/home/shared/auths/.env'
            self.dbType = 'database'
            self.insert_list_file = 'table_config.json'
            self.insert_list_path = os.path.join(self.tables_dir,'table_config.json')
            self.repo={}
    def var_check(self,dbName,dbType=None):
        dbType= dbType or self.dbType
        if dbName not in self.repo:
            self.repo[dbName]={}
        if dbType not in self.repo[dbName]:
            self.repo[dbName][dbType]={
                "env_path":self.env_path,
                "tables_dir":self.tables_dir,
                "insert_list_file":self.insert_list_file,
                "insert_list_path":self.insert_list_path
                }           
    def add_to_memory(self,dbName,dbType=None,env_path=None,tables_dir=None):
        dbType= dbType or self.dbType
        self.var_check(dbName,dbType=dbType)
        env_path = env_path or self.repo[dbName][dbType]["env_path"]
        tables_dir = tables_dir or self.repo[dbName][dbType]["tables_dir"]
        insert_list_file = create_insert_list_file(dbName,dbType=dbType) or self.repo[dbName][dbType]["insert_list_file"]
        insert_list_path = os.path.join(tables_dir,insert_list_file) or self.repo[dbName][dbType]["insert_list_path"]
        dbValues = self.get_db_values(dbName,dbType=dbType,env_path=env_path)
        self.repo[dbName][dbType]={
            "env_path":env_path,
            "tables_dir":tables_dir,
            "db_values":dbValues,
            "insert_list_file":insert_list_file,
            "insert_list_path":insert_list_path,
            }
    def get_from_memory(self,dbName,dbType=None,variable=None):
        dbType= dbType or self.dbType
        self.var_check(dbName,dbType=dbType)
        return self.repo[dbName][dbType].get(variable,self.repo[dbName][dbType])
    def get_db_values(self,dbName,dbType=None,env_path=None):
        dbType= dbType or self.dbType
        env_path = env_path or self.get_from_memory(dbName,dbType=dbType,variable="env_path")
        keys = {"user":None,"dbname":None,"host":None,"port":None,"password":None}
        for key,value in keys.items():
            keys[key]=get_pure_env_value(key=get_db_key(dbName,dbType,key),path=env_path)
        return keys
    def get_conn_mgr(self,dbName,dbType=None,env_path=None,tables=None):
        dbType= dbType or self.dbType
        return connectionManager(dbName=dbName,
                             dbType=dbType,
                             env_path=env_path or self.get_from_memory(self,dbName,dbType=dbType,variable="env_path"),
                             tables=tables or get_insert_list(dbName,dbType=dbType))
def get_tables_dir(dbName,dbType=None):
    tables_dir = envManager().tables_dir
    if dbName:
        tables_dir = envManager().get_from_memory(dbName,dbType=dbType,variable="tables_dir")
    return tables_dir
def get_env_path(dbName,dbType=None):
    env_path = envManager().env_path
    if dbName:
        env_path = envManager().get_from_memory(dbName,dbType=dbType,variable="env_path")
    return env_path
def get_insert_list_path(dbName,dbType=None):
    insert_list_path = envManager().insert_list_path
    if dbName:
        insert_list_path = envManager().get_from_memory(dbName,dbType=dbType,variable="insert_list_path")
    return insert_list_path
def get_insert_list(dbName,dbType=None):
    return safe_read_from_json(get_insert_list_path(dbName=dbName,dbType=dbType))
def get_conn_mgr(dbName,dbType=None,env_path=None,tables=None):
    return envManager().get_conn_mgr(dbName,dbType=dbType,env_path=env_path,tables=tables)
def getInsertType(tableName=None,table_configurations=None,dbName=None,dbType=None):
    table_configurations = table_configurations or get_insert_list(dbName=dbName,dbType=dbType)
    insertList = [ls for ls in table_configurations if ls.get("tableName").lower() == tableName.lower()]
    return insertList[0] if insertList else None
def dump_if_dict(obj):
    if isinstance(obj,dict):
        obj = json.dumps(obj)
    return obj
