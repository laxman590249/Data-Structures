time_zones = {'PST': 'America/Los_Angeles', 'EST':' America/New_York', 'CST': 'America/Chicago', 'MST': 'America/Denver'}

vars="\"{'custom_sql': \\\"and cc.timezone='CST'\\\", 'locale':'us', 'timezone':'America/Chicago'}\""
dbt_cmd_snapshot="""dbt run --project-dir=/airflow/dbt/ticketing/ --profiles-dir=/airflow/dbt/ --models inventory_snapshot --vars %s"""%(vars)
print(dbt_cmd_snapshot)

us_dbt_ticketing_manual__customsql  = ' and context_id = 123654'
for timezones, time_zones_fullform in time_zones.items():
	option = ''
	custom_sql = f" \\\"and cc.timezone='{timezones}' {us_dbt_ticketing_manual__customsql} \\\" "
	print(custom_sql)
	dbt_cmd_snapshot = """dbt run --project-dir=/airflow/dbt/ticketing/ %s --profiles-dir=/airflow/dbt/ --models inventory_snapshot --vars \"{'custom_sql': %s, 'locale':'us', 'timezone': %s}\"""" % (
	option, custom_sql, time_zones_fullform)
	print(dbt_cmd_snapshot)


