
import pymysql
import sys
import sqlparse

def db_info():
    try:
        db = pymysql.connect(host="10.10.10.175", user="root", password="root", database="dbmanager", port=3306,charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("select  DISTINCT db_type from db_info")
        dbtype = cursor.fetchall()
        #print(dbtype)
        for i in range(len(dbtype)):
            if dbtype[i]['db_type'].lower() == 'mysql':
                sql ="select HOST, PORT,DB_NAME,USER, PASSWORD,CHARSET from db_info where db_type='Mysql'"
                #print(sql)
                cursor.execute(sql)
                dbinfo = cursor.fetchall()
                return dbinfo
    except pymysql.Error as e:
        print(e)
    finally:

        cursor.close()
        db.commit()
        db.close()



def exec_sql(sql,dbinfo):
    try:
        for i in range(len(result)):
            host = bytes.decode(dbinfo[i]["HOST"])
            port = dbinfo[i]["PORT"]
            database = dbinfo[i]["DB_NAME"]
            user = dbinfo[i]["USER"]
            password = dbinfo[i]["PASSWORD"]
            charset = dbinfo[i]["CHARSET"]
            #dbinfo="host="%s"%(host), user="%s"%(user), password="%s"%(password), database="%s"%(database), port="%d"%(port)"
            print (database)
            db = pymysql.connect(host="%s"%(host), user="%s"%(user), password="%s"%(password), database="%s"%(database), port=port,
                                 cursorclass=pymysql.cursors.DictCursor)
            cursor = db.cursor()
            for j in range(len(sql)):
                cursor.execute(sql[j])
                data = cursor.fetchall()
            print(data)
    except pymysql.Error as e:
        print(e)
    finally:

        cursor.close()
        db.commit()
        db.close()



def sql_parse(sql):

    sqlp=sqlparse.split(sql)
    return sqlp


sql1="set sql_log_bin=0;\n show variables like '%sql_log_bin%'"
#print(sql1)
sql=sql_parse(sql1)
#print(sql)
result=db_info()
exec = exec_sql(sql=sql,dbinfo=result)
