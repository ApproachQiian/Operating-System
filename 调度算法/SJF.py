"""
short job first algorithm
author:jian
"""


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


def main():
    pass


if __name__ == '__main__':
    Nodes = []
    main()
