# -*- coding: utf-8 -*-
import threading
from socket import *

lock = threading.Lock()
openNum = 0
threads = []
allopenport = []


def portScanner(host, port):
    global openNum
    global allopenport

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        # 创建多线程互斥锁
        lock.acquire()
        # 这个时候应该已经开始了，不通的直接pass，通的继续执行
        openNum += 1
        # 只要这个端口开着，就会被输出
        # print('[+] %d open' % port)
        allopenport.append(port)
        # print(port)
        # 释放锁
        lock.release()
        # 关闭socket
        s.close()
    except:
        # 将关闭的端口也输出
        # print('[-] %d close' % port)
        pass


def main(host):
    # 设置默认超时时间为1s
    setdefaulttimeout(1)
    # 开始依次扫描-H后面的主机，默认扫描全部端口，可修改
    for p in range(0, 65535):
        # 定义t，开启多线程，大意是开启p的最大值个线程，去跑portScaner
        t = threading.Thread(target=portScanner, args=(host, p))
        # 这个是将t的值写道threads里面
        threads.append(t)
        # 这个地方真正开始调用portScanner
        t.start()
    # 这个循环确保以上循环的全部线程跑完才会向下继续执行！！！如果将t.join加入到以上循环，则会按顺序输出，但是多线程就没有了意义，依次执行了。
    for t in threads:
        t.join()
    # 以下是返回
    return allopenport
