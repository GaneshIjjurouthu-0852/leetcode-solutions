from collections import deque
class MyStack(object):
    def __init__(self):
        self.que=deque()
    def push(self,x):
        self.que.append(x)
        n=len(self.que)
        for _ in range(n-1):
            self.que.append(self.que.popleft())
    def pop(self):
        return self.que.popleft()
    def top(self):
        return self.que[0]
    def empty(self):
        if len(self.que)==0:
            return True
        return False
