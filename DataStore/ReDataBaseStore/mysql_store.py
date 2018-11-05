# -*- coding: utf-8 -*-
import pymysql


def connect_to_mysql():
    db = pymysql.connect(host='localhost', user='root', password='mysql', port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print('Database version:', data)
    cursor.execute("CREATE DATABASE myspiders DEFAULT CHARACTER SET utf8")
    db.close()


def connect_to_database_in_mysql():
    db = pymysql.connect(host='localhost', user='root', password='mysql', port=3306, db='myspiders')
    cursor = db.cursor()
    sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) not NULL, name VARCHAR(255) NOT NULL, age INT NOT " \
          "NULL, PRIMARY KEY (id))"
    cursor.execute(sql)
    db.close()
    pass


if __name__ == '__main__':
    connect_to_database_in_mysql()
    # connect_to_mysql()
