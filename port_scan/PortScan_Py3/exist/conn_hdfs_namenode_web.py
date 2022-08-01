# coding=UTF-8
from hdfs.client import Client


def find_hadoop_datanode():
    client = Client('http://192.168.130.103:50070', timeout=2)
    rows = len(client.list('/'))
    print(rows)


if __name__ == '__main__':
    find_hadoop_datanode()
