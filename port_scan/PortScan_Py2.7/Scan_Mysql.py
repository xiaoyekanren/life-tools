# coding=UTF-8
import pymysql
import threading
import sys

threads = []
mysql_port = 0
ccc = 'usingpassword'


def mysql_Scan(tsoh, trop):
    global mysql_port
    try:
        connection = pymysql.connect(host=tsoh, user='gsfdsa', password='password', db='user', connect_timeout=1, port=trop, read_timeout=1, write_timeout=1)
    except BaseException as be:
        be = bytes(be).replace(' ', '')
        if ccc in be:
            mysql_port = trop
        else:
            sys.exit(0)


def mysql(host, openedports):
    for p in openedports:
        t = threading.Thread(target=mysql_Scan, args=(host, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # print type(mysql_port)
    return mysql_port
