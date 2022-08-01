# coding=UTF-8
import argparse
import sys

import port_scan
from exist import conn_cassandra, conn_pg, conn_mysql, conn_hdfs_datanode, conn_hdfs_namenode_web


def main():
    # #定义参数描述
    p = argparse.ArgumentParser(description="Zzm's main Program")
    ## 添加参数-H or --host
    p.add_argument('-H', '--host', dest='hosts', type=str, help='write a ip address')
    args = p.parse_args()
    hosts = args.hosts
    # 查看输入的ip
    # print hosts

    ###定义实际各项服务的值
    hadoop_defaultfs_port = ''
    hadoop_namenode_web_port = ''
    mysql_port = ''
    cassandra_port = ''
    postgresql_port = ''

    # 判断有没有传回参数,没有则直接退出
    if len(sys.argv) < 2:
        print('Error:mush add a parameter,use --help to view help information')
        sys.exit()
    # 输出本文件执行时文件名后面参数的长度
    # print len(sys.argv)

    # 执行Scan_Socket.py的main函数，扫描该IP的全部端口
    openedports = port_scan.main(hosts)
    print("Port is open:  ", bytes(openedports))
    print('A total of ', bytes(len(openedports)))
    # ---------------------
    # 此循环用于扫描hdfs的50070端口
    print('start to find hadoop-50070.....')
    for port in openedports:
        try:
            # conn_hdfs_namenode_web.py的main函数，确定哪个是50070端口
            conn_hdfs_namenode_web.main(hosts, bytes(port))
            # print(bytes(port) + ' is Hadoop-Namenode-Web-Port(Defaults is 50070)')
            ##已经找到端口，移除该端口，便于一下循环
            openedports.remove(port)
            hadoop_namenode_web_port = bytes(port)
            break
        # 这个地方应该在except后面指定错误信息，但是不知道错误信息是啥。所以只要报错就会跳出本次循环
        except:
            continue
            # pass
    # 输出看下是否移除了hdfs_namenode的端口
    # print(bytes(openedports))
    # print ('A total of ' + bytes(len(openedports)))
    # ------------------------------
    # 此循环用于扫描hdfs的9000端口
    print('start to find hadoop-9000.....')
    for port in openedports:
        try:
            conn_hdfs_datanode.main(hosts, port)
            # print(bytes(port) + ' is Hadoop-defaultFS-Port(Defaults is 9000)')
            openedports.remove(port)
            hadoop_defaultfs_port = bytes(port)
            break
        except:
            continue
        # #没有实现
        # else:
        #     print('MeiYouZhaoDao')
    # 输出看下是否移除了hdsf_namenode的端口
    # print(bytes(openedports))
    # print ('A total of ' + bytes(len(openedports)))
    # -----------------------------
    # 此循环用于扫描Mysql的3306端口
    print('start to find mysql-3306.....')
    for port in openedports:
        if conn_mysql.main(hosts, port) == 1:
            # print(bytes(port) + ' is MySql-Port(Defaults is 3306)')
            openedports.remove(port)
            mysql_port = bytes(port)
            break
        else:
            continue
    # 输出看下是否移除了Mysql的3306端口
    # print(bytes(openedports))
    # print ('A total of ' + bytes(len(openedports)))
    # ----------------------------------
    # 此循环用于扫描Cassandra的9042端口
    print('start to find cassandra-9042.....')
    for port in openedports:
        if conn_cassandra.main(hosts, port) == 1:
            # print(bytes(port) + ' is Cassandra-Port(Defaults is 9042)')
            openedports.remove(port)
            cassandra_port = bytes(port)
            # WARN:这个地方加break可以减少等待时间，但是会在后面报错
            # break
        else:
            continue
    # ----------------------------------
    # 此循环用于扫描Postgresql的5432端口
    print('start to find postgresql-5432.....')
    for port in openedports:
        if conn_pg.main(hosts, port) == 1:
            openedports.remove(port)
            postgresql_port = bytes(port)
        else:
            continue
    # print(bytes(openedports))
    # print ('A total of ' + bytes(len(openedports)))
    # ----------------------------------
    print('-----------------------------')
    if hadoop_defaultfs_port == '':
        print('Hadoop-DefaultFS-port is not find!')
    else:
        print('Hadoop-DefaultFS-Port: ', hadoop_defaultfs_port)
    # ---------
    if hadoop_namenode_web_port == '':
        print('Hadoop-Namenode-Web-Port is not find!')
    else:
        print('Hadoop-Namenode-Web-Port: ', hadoop_namenode_web_port)
    # ---------
    if mysql_port == '':
        print('Mysql-Port is not find!')
    else:
        print('Mysql-Port: ', mysql_port)
    # ---------
    if cassandra_port == '':
        print('Cassandra-Port is not find!')
    else:
        print('Cassandra-Port: ', cassandra_port)
    # ---------
    if postgresql_port == '':
        print('Postgresql-Port is not find!')
    else:
        print('Postgresql-Port: ', postgresql_port)


if __name__ == '__main__':
    main()
