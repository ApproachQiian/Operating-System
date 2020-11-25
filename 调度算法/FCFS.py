class Node(object):
    def __init__(self):
        self.arriveTime = 0  # 到达时间
        self.serviceTime = 0  # 要求服务时间
        self.startTime = 0  # 开始运行时间
        self.endTime = 0  # 结束运行时间
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
    global endTime
    for i in range(len(Nodes)):
        pid = i + 1
        if i == 0:
            startTime = Nodes[i].arriveTime
            endTime = Nodes[i].arriveTime + Nodes[i].serviceTime
        else:
            startTime = endTime + 1
            endTime += (Nodes[i].serviceTime + 1)
        waitTime = endTime - Nodes[i].arriveTime  # 周转时间= 结束运行时间-到达时间
        averageTime = waitTime / Nodes[i].serviceTime  # 带权周转时间=周转时间/服务时间
        printTask(pid, startTime, waitTime, averageTime, endTime)


def printTask(pid, startTime, waitTime, averageTime, endTime):
    Nodes[pid - 1].startTime = startTime
    Nodes[pid - 1].waitTime = waitTime
    Nodes[pid - 1].averageTime = averageTime
    Nodes[pid - 1].endTime = endTime
    print('进程{}的到达时间:{}'.format(pid, Nodes[pid - 1].arriveTime))
    print('进程{}的要求服务时间:{}'.format(pid, Nodes[pid - 1].serviceTime))
    print('进程{}的开始运行时间:{}'.format(pid, Nodes[pid - 1].startTime))
    print('进程{}的结束运行时间:{}'.format(pid, Nodes[pid - 1].endTime))
    print('进程{}的周转时间时间:{}'.format(pid, Nodes[pid - 1].waitTime))
    print('进程{}的带权周转时间:{}'.format(pid, Nodes[pid - 1].averageTime))
    print('*' * 30)


def main():
    print('***请输入需要运行的进程个数***')
    n = int(input())
    for pid in range(1, n + 1):
        readTask(pid)
    runTask()


if __name__ == '__main__':
    Nodes = []
    main()
