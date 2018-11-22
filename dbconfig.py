import pymysql
import sys
import time
from managerdbinfo import db_info,sql


def mysql_conn():
    return pymysql.connect(**dbinfo)


class dbinfo(object):
    def __init__(self, dbinfo):
        self.dbinfo = dbinfo
        self.conn = self.__get_connection(dbinfo)
    def __get_connection(self,dbinfo):
        dbconn = None
        while True:
            try:
                dbconn = pymysql.Connect(**dbinfo)
            except pymysql.Error as e:
                print("MySQL.Error: {0}".format(e))
                '''
                if e.args[0] == 2003:
                    time.sleep(2)
                else:
                    sys.exit(2)
                '''
                sys.exit(2)
            else:
                return dbconn

    def query(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            cur.close()
        except pymysql.Error as e:
            # try again with new connection
            if e.args[0] in (2013, 2003):
                print("MySQL.Error: {0} (retry)".format(e))
                sys.exit(2)
            elif e.args[0] in (1205, 1213):
                # deadlock found, or lock wait timeout
                print("MySQL.Error: {0} (retry)".format(e))
                print("  %s [%s]" % (sql))
                sys.exit(2)
            else:
                print("MySQL.Error: {0} (skip)".format(e))
                print("  %s [%s]" % (sql))
                # print and skip
                return -1
        except KeyboardInterrupt:
            # requeue
            return -2

        print(data)
sql = "select * from db_info"
p=dbinfo(db_info)
p1=dbinfo.query(self=None,sql=sql)






