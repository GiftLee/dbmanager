sql="set sql_log_bin=0;\r\nshow variables \nlike '%log_bin%'"
print(sql)
sql_list = sql.split(';')
sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
print(type(sql_list))
print(sql_list[0])
print(sql_list[1])
