# coding=UTF-8
from psycopg2 import connect as pg_client
import threading

threads = []
pg_port = 0


def pg_Scan(ip, trop):
    global pg_port
    auth = 'passwordauthentication'
    try:
        conn = pg_client(database="postgres", user="postgres", password="*", host=ip, port=trop, connect_timeout=1)
        # print "connect success"
    except BaseException as be:
        # print be
        if auth in bytes(be).replace(' ', ''):
            # return 1
            pg_port = trop
        else:
            return 0


def pg(host, openedports):
    for p in openedports:
        t = threading.Thread(target=pg_Scan, args=(host, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # print type(pg_port)
    return pg_port
