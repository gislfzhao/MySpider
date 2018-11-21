# -*- coding: utf-8 -*-
import pymysql

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'mysql'
MYSQL_DATABASE = 'weixin'


class MySQL:
    def __init__(self, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD,
                 database=MYSQL_DATABASE):
        """
        MySQL初始化
        :param host:
        :param port:
        :param username:
        :param password:
        :param database:
        """
        try:
            db = pymysql.connect(host=host, user=user, password=password, port=port)
            cursor = db.cursor()
            if not cursor.execute("SELECT * FROM information_schema.SCHEMATA where SCHEMA_NAME='" + database
                                  + "'"):
                sql_create_db = "Create Database " + database
                cursor.execute(sql_create_db)
            del db, cursor
            self.db = pymysql.connect(host=host, user=user, password=password, port=port, database=database,
                                      charset='UTF8MB4')
            self.cursor = self.db.cursor()
            self.create_table('article')
        except pymysql.MySQLError as e:
            print(e.args)

    def create_table(self, table):
        """
        创建表
        :param table: 表名
        :return:
        """
        sql_create_table = "CREATE TABLE IF NOT EXISTS " + table + \
                           "(id INT(11) NOT NULL AUTO_INCREMENT," \
                           "title VARCHAR(255) NOT NULL," \
                           "content TEXT NOT NULL," \
                           "date VARCHAR(255)," \
                           "wechat VARCHAR(255)," \
                           "nickname VARCHAR(255)," \
                           "label TEXT," \
                           "PRIMARY KEY (id))"
        self.cursor.execute(sql_create_table)

    def insert(self, table, data):
        """
        插入数据
        :param table: 表名
        :param data: 数据
        :return:
        """
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql_query = 'INSERT INTO %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.db.close()

# if __name__ == '__main__':
#     p = MySQL()
#     p.create_table('art')
#     p.insert('art', data)
#     p.close()
