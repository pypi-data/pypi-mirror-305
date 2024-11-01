import json
from abstract_database import *
from abstract_solana import Client,get_insert_list
from abstract_utilities import SingletonMeta,safe_read_from_json
from abstract_apis import postRpcRequest,get_async_response,postRequest
from ...utils import getSolcatcherUrl
from ...abstract_rate_limit import get_rate_limit_url,log_response
async def getSolcatcherPost(endpoint, *args, **kwargs):
    # Ensure that the arguments are fully resolved and not coroutines
    resolved_args = [await arg if asyncio.iscoroutine(arg) else arg for arg in args]
    
    # Check for coroutines in kwargs and resolve them without reusing
    resolved_kwargs = {}
    for k, v in kwargs.items():
        if asyncio.iscoroutine(v):
            resolved_kwargs[k] = await v
        else:
            resolved_kwargs[k] = v
    
    # Now pass resolved data into the request
    return await asyncPostRequest(
        url=getSolcatcherUrl(),
        endpoint=endpoint,
        data={"args": resolved_args, **resolved_kwargs}
    )
def make_single(string):
  return string.replace('_','')
def get_env_mgr(dbName,tables_dir,insert_list_file,env_path):
    # Existing utility functions remain the same
    # Constants
    env_mgr = envManager()
    insert_list_path = os.path.join(tables_dir,insert_list_file)
    tables = safe_read_from_json(insert_list_path)
    insert_list_path = os.path.join(tables_dir)
    env_mgr.add_to_memory(dbName = dbName,dbType='database',
                          env_path=env_path,
                          tables_dir=tables_dir,
                          insert_list_file = insert_list_file,
                          insert_list_path=insert_list_path,
                          tables=tables,
                          table={'':''})
def get_data_from_dbName(dbName,tableName,dbType=None,variable=None):
  variables={}
  tableName = make_single(tableName)
  variables['tables'] = envManager().get_from_memory(dbName, variable='tables')
  variables['table'] = [table for table in variables['tables'] if table.get('tableName') == tableName]
  if variables['table']:
    variables['table'] = variables['table'][0]
  variables['tableName'] = variables['table'].get('tableName')
  variables['insertName'] = variables['table'].get("columnSearch")
  if variable:
      variables = variables['table'].get(variable)
  return variables
dbName = 'solcatcher'
tables_dir='/home/computron/Desktop/solcatcher/api/test/'
insert_list_file='solana_db_tables.json'
env_path='/home/computron/Desktop/solcatcher/api/test/.env'
env_mgr = get_env_mgr(dbName,tables_dir,insert_list_file,env_path)
def get_call_url(method):
  urls = get_rate_limit_url(method)
  return urls.get('url')
class clientMgr(metaclass=SingletonMeta):
  def __init__(self):
    if not hasattr(self, 'initialized'):  # Prevent reinitialization
      self.initialized = True
      self.client = Client()
      self.functions={}
  def get_client_function(self,method):
    if method not in self.functions:
      self.functions[method]=getattr(self.client,method)
    return self.functions[method]
  def get_body(self,method,*args,**kwargs):
    function = self.get_client_function(method)
    return function(*args,**kwargs)
  def get_partial_call(self,method,body):
    url = get_call_url(method)
    response = postRpcRequest(url,**body)
    log_response(method, response)
    return response
  def call_solana(self,method,*args,**kwargs):
    body = self.get_body(method,*args,**kwargs)
    response = self.get_partial_call(method,body)
    return response
def call_solana(method,*args,**kwargs):
  return clientMgr().call_solana(method,*args,**kwargs)
def get_body(method,*args,**kwargs):
  return clientMgr().get_body(method,*args,**kwargs)
def partial_call_solana(method,body):
  return clientMgr().get_partial_call(method,body)
def get_rate_limit(method):
    return get_call_url(method)
def get_log_response(method,response={}):
    return log_response(method,response)
def insert_db(*args,**kwargs):
    return get_async_response(getSolcatcherPost,'insert_into_db',*args,**kwargs)
def fetch_from_db(*args,**kwargs):
    return get_async_response(getSolcatcherPost,'fetch_from_db',*args,**kwargs)
def call_solcatcher_api(*args,**kwargs):
    return get_async_response(getSolcatcherPost,'/api/v1/rpc_call',*args,**kwargs)
def call_solcatcher_db_api(method,*args,**kwargs):
    variables = get_data_from_dbName('solcatcher',method)
    insertTable = variables['table']
    freshCall = insertTable.get('freshCall')
    tableName=insertTable.get('tableName')
    if insertTable.get('rpcCall'):
        rpc_dict = get_body(method,*args,**kwargs)
        searchValue=rpc_dict.get('params')[0]
        if not freshCall:
            insertValue  = fetch_from_db(tableName=tableName,searchValue=searchValue)
            if insertValue:
                return insertValue
        insertValue = partial_call_solana(method,rpc_dict)
        get_log_response(method,insertValue)
        insert_db(tableName=tableName,searchValue=searchValue,insertValue=insertValue)
        return insertValue
    else:
        searchValue= args[0] if args else None
        if not freshCall:
            insertValue  = fetch_from_db(tableName=tableName,searchValue=searchValue)
            if insertValue:
                return insertValue
        insertValue = postRequest(url=f'{getSolcatcherUrl()}/{method}',data=json.dumps({"args":args,**kwargs}))
        get_log_response(method,insertValue)
        insert_db(tableName=tableName,searchValue=searchValue,insertValue=insertValue)
        return insertValue    
    return response
