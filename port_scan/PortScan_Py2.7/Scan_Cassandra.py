# coding=UTF-8
from cassandra.cluster import Cluster as cassandra_Cluster
import threading
import sys

threads = []
cassandra_port = 0


def cassandra_Scan(host, p):
    global cassandra_port
    client = cassandra_Cluster([host], port=p, connect_timeout=2)
    try:
        session = client.connect('system_traces')
        rows = session.execute('select * from sessions;')
        cassandra_port = p
    except:
        # return 0
        sys.exit(0)


def cassandra(host, openedports):
    for p in openedports:
        t = threading.Thread(target=cassandra_Scan, args=(host, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return cassandra_port
