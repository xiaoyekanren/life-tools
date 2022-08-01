# coding=UTF-8
import pymysql


def find_mysql_port():
    host = '192.168.130.103'
    port = 3306
    connection = pymysql.connect(host=host,
                                 user='root',
                                 password='123456',
                                 db='test',
                                 connect_timeout=1,
                                 port=port,
                                 read_timeout=1,
                                 write_timeout=1)
    cur = connection.cursor()
    cur.execute('select * from test1;')
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    find_mysql_port()
