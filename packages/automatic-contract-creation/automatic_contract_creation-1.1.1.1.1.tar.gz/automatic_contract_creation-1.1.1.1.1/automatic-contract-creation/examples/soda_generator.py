from automatic_contract_creation.scr.generators.soda_generator import SODAGenerator

creds_trino = {
    'host': 'host',
    'port': 8443,
    'user': 'username',
    'password': 'password',
    'catalog': 'catalogname',
    'schema': 'schemaname'
}

query_trino = 'select * from catalogname.schemaname.tablename where price>10 limit 10000'

soda = SODAGenerator(connection_name='trino', **creds_trino)
soda.generate_soda_contracts(query_trino)



