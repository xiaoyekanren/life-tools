# coding=UTF-8
import argparse
import sys
import Scan_Socket
import Scan_Cassandra
import Scan_Hadoop
import Scan_Mysql
import Scan_Postgresql


def main():
    # #定义参数描述
    p = argparse.ArgumentParser(description="Zzm's main Program")
    # 添加参数-H or --host
    p.add_argument('-H', '--host', dest='hosts', type=str, help='write a ip address')
    args = p.parse_args()
    hosts = args.hosts

    # 判断有没有传回参数,没有则直接退出
    if len(sys.argv) < 2:
        print('Error:mush add a parameter,use --help to view help information')
        sys.exit()
    # 输出本文件执行时文件名后面参数的长度
    # print len(sys.argv)

    # -----------------------------
    # 执行Scan_Socket.py的main函数，扫描该IP的全部端口
    openedports = Scan_Socket.main(hosts)
    print("Port is open:  " + bytes(openedports))
    print('A total of ' + bytes(len(openedports)))

    # ----------------------------------
    # 扫描Cassandra的9042端口
    print('start to find Cassandra-Port.....')
    Cassandra_realport = Scan_Cassandra.cassandra(hosts, openedports)
    if Cassandra_realport != 0:
        openedports.remove(Cassandra_realport)
        print('Cassandra-Port: ' + bytes(Cassandra_realport))
    else:
        print('Cassandra-Port is not find!')
    # -----------------------------
    # 扫描hdfs的50070端口
    print('start to find Hadoop-Namenode-Port.....')
    Hadoop_namenode_realport = Scan_Hadoop.hdfs50070(hosts, openedports)
    if Hadoop_namenode_realport != 0:
        openedports.remove(Hadoop_namenode_realport)
        print('Hadoop-Namenode-Port: ' + bytes(Hadoop_namenode_realport))
    else:
        print('Hadoop-Namenode-Port is not find!')
    # -----------------------------
    # 扫描hdfs的9000端口
    print('start to find Hadoop-Datanode-Port.....')
    Hadoop_datanode_realport = Scan_Hadoop.hdfs9000(hosts, openedports)
    if Hadoop_datanode_realport != 0:
        openedports.remove(Hadoop_datanode_realport)
        print('Hadoop-Datanode-Port: ' + bytes(Hadoop_datanode_realport))
    else:
        print('Hadoop-Datanode-Port is not find!')
    # -----------------------------
    # 扫描Postgresql的5432端口
    print('start to find Postgresql-Port.....')
    pg_port = Scan_Postgresql.pg(hosts, openedports)
    if pg_port != 0:
        openedports.remove(pg_port)
        print('Postgresql-Port: ' + bytes(pg_port))
    else:
        print('Postgresql-Port is not find!')
    # -----------------------------
    # 扫描Mysql的3306端口
    print('start to find Mysql-Port.....')
    mysql_port = Scan_Mysql.mysql(hosts, openedports)
    if mysql_port != 0:
        openedports.remove(mysql_port)
        print('Mysql-Port: ' + bytes(mysql_port))
    else:
        print('Mysql-Port is not find!')


if __name__ == '__main__':
    main()
