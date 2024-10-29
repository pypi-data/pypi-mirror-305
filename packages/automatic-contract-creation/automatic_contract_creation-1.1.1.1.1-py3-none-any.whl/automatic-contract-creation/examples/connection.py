from automatic_contract_creation.scr.connectors.connection_manager import ConnectionManager

creds_click = {'user':'username',
               'password' : 'password',
               'host' : 'host',
               'port' : 8000,
               'db_name' : 'shemaname'
              }

query_click = 'select * from shemaname.click_table limit 100'

con_obj = ConnectionManager('clickhouse',  **creds_click)
data_click = con_obj.read_data(query_click).collect()



creds_trino = {
    'host': 'host',
    'port': 8443,
    'user': 'username',
    'password': 'password',
    'catalog': 'catalognamne',
    'schema': 'schemaname'

}

query_trino= 'select * from catalognamne.schemaname.trino_table where site=? limit 100'
connection_trino = con_obj('trino', **creds_trino)
data_trino = connection_trino.read_data(query_trino, ['RU'])







