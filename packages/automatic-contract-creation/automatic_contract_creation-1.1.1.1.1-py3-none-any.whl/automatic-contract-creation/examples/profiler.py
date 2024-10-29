from automatic_contract_creation.scr.profilers.profiler import Profiler as pr



creds_trino = {
    'host': 'host',
    'port': 8443,
    'user': 'username',
    'password': 'password',
    'catalog': 'catalogname',
    'schema': 'schemaname'
}


query_trino = 'select * from catalogname.schemaname.tablename limit 1000'


con = pr(connection_name='trino', **creds_trino)
data = con.read_data(query_trino)

metrics = con.compute_metrics(lazyframe=data, dt='update_dt')

con.save_to_csv(lazyframe=data, dt='update_dt')
print(metrics)


