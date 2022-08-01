# coding=UTF-8
from cassandra.cluster import Cluster


def find_cassandra_cql_port():
    cluser = Cluster(['192.168.130.103'], port=9042, connect_timeout=5)
    session = cluser.connect('system_schema')
    rows = session.execute('select * from columns;')
    for row in rows:
        print(row)


if __name__ == '__main__':
    find_cassandra_cql_port()