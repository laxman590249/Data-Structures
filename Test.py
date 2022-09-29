data = """305674245:32325025:3	305674245:32325025	305674245	32325025	1	-1	3	(737)444-3314	FALSE		40:12.8	2022-09-07 15:27:15.740 +0000
305674245:32325093:3	305674245:32325093	305674245	32325093	1	-1	3	(323)219-1515	FALSE		39:52.7	2022-09-07 15:27:15.740 +0000
305674245:32325130:3	305674245:32325130	305674245	32325130	1	-1	3	(405)613-7322	FALSE		45:19.1	2022-09-07 15:27:15.740 +0000
305674245:32325209:3	305674245:32325209	305674245	32325209	1	-1	3	(626)315-8800	FALSE		41:16.5	2022-09-07 15:27:15.740 +0000"""

data_type_string = """CUSTOMER_PHONE_UNIQUE_ID	VARCHAR(16777216)
CUSTOMER_UNIQUE_ID	VARCHAR(50)
CONTEXT_ID	NUMBER(38,0)
CUSTOMER_ID	NUMBER(38,0)
COUNTRY_CODE	VARCHAR(20)
PHONE_TYPE_ID	NUMBER(38,0)
PHONE_PRIORITY	NUMBER(1,0)
PHONE	VARCHAR(16777216)
_IS_DELETED	BOOLEAN
_DELETED_DATETIME	TIMESTAMP_NTZ(9)
MODIFIED_DATETIME	TIMESTAMP_NTZ(9)
CREATED_ON	TIMESTAMP_LTZ(9)"""
data_type = []

for i in data_type_string.split('\n'):
    col = i.split('\t')
    data_type.append(col[1])
print(data_type)
print(len(data_type))


for i in data.split('\n'):
    print('(', end='')
    count = 0
    for index, j in enumerate(i.split('\t')):
        count += 1
        if 'NUMBER' in data_type[index]:
            if j:
                print(f'{j},', end='')
            else:
                print(f'0,', end='')
        elif j:
            print(f"'{j}',", end='')
        else:
            print("'',", end='')
    print('),')
    print('>>>', count)
