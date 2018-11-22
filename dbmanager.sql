##数据库初始化
CREATE DATABASE `dbmanager` DEFAULT CHARACTER SET utf8mb4 ;

CREATE TABLE dbmanager.DB_INFO (
  ID INT(10) NOT NULL AUTO_INCREMENT,
  HOST VARBINARY(20) NOT NULL ,
  PORT INT(5) NOT NULL ,
  DB_NAME VARCHAR(30) NOT NULL ,
  USER VARCHAR(20) NOT NULL ,
  PASSWORD VARCHAR(50) NOT NULL ,
  CHARSET VARCHAR(50) DEFAULT "utf8mb4",
  DB_TYPE VARCHAR(30) DEFAULT "Mysql",
 PRIMARY KEY (`ID`)
);

INSERT INTO dbmanager.DB_INFO(HOST, PORT,DB_NAME,USER, PASSWORD,CHARSET,DB_TYPE)
VALUE ("10.10.10.175",3306,"LAMBO","root","root","utf8mb4","Mysql");

INSERT INTO dbmanager.DB_INFO(HOST, PORT,DB_NAME,USER, PASSWORD,CHARSET,DB_TYPE)
VALUE ("10.10.250.149",3306,"LAMBO","root","root","utf8mb4","Mysql");

INSERT INTO dbmanager.DB_INFO(HOST, PORT,DB_NAME,USER, PASSWORD,CHARSET,DB_TYPE)
VALUE ("10.10.10.175",3306,"linshidb","root","root","utf8mb4","Mysql");

create table liwu ( `id`    INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT )
    db = pymysql.connect(host="10.10.10.175",user="root",password="root",database="dbmanager",port=3306,cursorclass = pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("select  db_type from db_info")
    dbtype =  cursor.fetchall()
    for i in range(len(dbtype)):
        if dbtype[i]['db_type'].lower() == 'mysql':
            cursor.execute("select HOST, PORT,DB_NAME,USER, PASSWORD,CHARSET from db_info")
            cursor.fetchall()
    cursor.close()
    db.close()