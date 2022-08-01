from snakebite.client import Client


def find_hadoop_defaultfs():
    client = Client("192.168.130.103", 9000, use_trash=False)
    for x in client.ls(['/']):
        print(x)


if __name__ == '__main__':
    find_hadoop_defaultfs()
