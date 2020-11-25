class Node(object):
    def __init__(self):
        self.arriveTime = 0  # 到达时间
        self.serviceTime = 0  # 要求服务时间
        self.startTime = 0  # 开始运行时间
        self.waitTime = 0  # 周转时间
        self.averageTime = 0  # 带权周转时间


def readTask(pid):
    node = Node()
    print('请输入第%d个进程的到达时间' % pid)
    node.arriveTime = float(input())
    print('请输入第%d个进程的要求服务时间' % pid)
    node.serviceTime = float(input())
    Nodes.append(node)


def runTask():
    pass


def printTask():
    pid = 1
    for node in Nodes:
        print('进程{}的到达时间:{}'.format(pid, node.arriveTime))
        print('进程{}的要求服务时间:{}'.format(pid, node.serviceTime))
        print('进程{}的开始运行时间:{}'.format(pid, node.startTime))
        print('进程{}的周转时间时间:{}'.format(pid, node.waitTime))
        print('进程{}的带权周转时间:{}'.format(pid, node.averageTime))
        print('*' * 20)
        pid += 1


def main():
    print('***请输入需要运行的进程个数***')
    n = int(input())
    for pid in range(1, n + 1):
        readTask(pid)
    runTask()
    printTask()


if __name__ == '__main__':
    Nodes = []
    main()
