# coding=UTF-8
from snakebite.client import Client as hdfs_client1
from hdfs import Client as hdfs_clietn2
import threading
import sys

threads = []
datanode_port = 0
namenode_port = 0



def hdfs50070(host, openedports):
    for p in openedports:
        t = threading.Thread(target=hdfs50070_Scan, args=(host, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return int(namenode_port)


def hdfs50070_Scan(ip, port):
    global namenode_port
    ipadd = ('http://' + ip + ':')
    client = hdfs_clietn2(ipadd + bytes(port), timeout=.1)  # port是字符型
    try:
        hdfs_clietn2.list(client, '/')
        namenode_port = port
    except:
        sys.exit(0)
    else:
        pass


def hdfs9000(host, openedports):
    for p in openedports:
        t = threading.Thread(target=hdfs9000_Scan, args=(host, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return datanode_port


def hdfs9000_Scan(host, port):
    global datanode_port
    try:
        client = hdfs_client1(host, port, sock_connect_timeout=2000, sock_request_timeout=2000)  # port是数值型
        for x in client.ls(['/']):
            break
        datanode_port = port
    # except IOError:  # 捕获的错误是错的
    except:
        sys.exit(0)
    else:
        pass


