# PortScan
------
## Function
A tool to Port Scan by Python2.7
Specify IP address,scan all ports,get the port's service
Current support:
> * Mysql:3306
> * Postgresql:5432
> * Cassandra:9042
> * hadoop:9000&50070
------
## Depends
### Python2.7:
> * cassandra-driver
> * snakebite
> * hdfs
> * pymysql
> * psycopg2
### Ubuntu:
```shell
 apt-get install python-dev
 apt-get install libmysqlclient-dev
 apt-get install gcc
```
------
## Start
```shell
 python Diaoyong.py --help
```