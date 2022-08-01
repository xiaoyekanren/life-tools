# coding=UTF-8
import psycopg2
import time


def find_pg_port():
    ip = '192.168.130.103'
    port = '5432'
    conn = psycopg2.connect(database="postgres", user="zzm", password="123456", host=ip, port=port, connect_timeout=1)
    cur = conn.cursor()
    cur.execute("select * from test;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        time.sleep(.05)


if __name__ == '__main__':
    find_pg_port()
