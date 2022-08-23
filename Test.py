LIMIT_ERROR = 'LIMIT_ERROR'
print()


slack_error_info = {
    ":heavy_exclamation_mark:CATEGORY": "15,  50%",
    ":heavy_exclamation_mark:CLIENTS": "15,  50%",
    ":heavy_exclamation_mark:CUSTOMERADDRESSES": "15,  50%",
    "        TIXEVENTZONESEATS": "15,  50%"
}
target_schema = 'QLA'
#
# max = max([len(i) for i in d.keys()])
#
# for i, j in d.items():
#     print(i.ljust(max) + ':  ' + j)

max_length = max([len(table_name) for table_name in slack_error_info.keys()])
data = f'*SCHEMA: {target_schema.upper()}*\n'+'\n'.\
                    join([f"{table}: {value}" for table, value in slack_error_info.items()])
print(data)