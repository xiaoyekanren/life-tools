# coding=UTF-8
from time import sleep
# ---------
from cassandra.cluster import Cluster as cassandra_connect
from psycopg2 import connect as pg_connect
from pymysql import connect as mysql_connect
from snakebite.client import Client as hdfs_defaultfs_connect
from hdfs.client import Client as hdfs_namenode_connect


def find_cassandra_cql_port():
    cluser = cassandra_connect(['192.168.130.103'], port=9042, connect_timeout=5)
    session = cluser.connect('system_schema')
    rows = session.execute('select * from columns;')
    for row in rows:
        print(row)


def find_pg_port():
    ip = '192.168.130.103'
    port = '5432'
    conn = pg_connect(database="postgres", user="zzm", password="123456", host=ip, port=port, connect_timeout=1)
    cur = conn.cursor()
    cur.execute("select * from test;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        sleep(.05)


def find_mysql_port():
    host = '192.168.130.103'
    port = 3306
    connection = mysql_connect(host=host, user='root', password='123456', db='test', connect_timeout=1, port=port, read_timeout=1, write_timeout=1)
    cur = connection.cursor()
    cur.execute('select * from test1;')
    rows = cur.fetchall()
    for row in rows:
        print(row)


def find_hadoop_defaultfs():
    client = hdfs_defaultfs_connect("192.168.130.103", 9000, use_trash=False)
    for x in client.ls(['/']):
        print(x)


def find_hadoop_datanode():
    client = hdfs_namenode_connect('http://192.168.130.103:50070', timeout=2)
    rows = len(client.list('/'))
    print(rows)
