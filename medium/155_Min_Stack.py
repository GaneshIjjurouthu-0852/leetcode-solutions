class MinStack(object):
    def __init__(self):
        self.mainstack=[]
        self.minstack=[]
    def push(self,val):
        self.mainstack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            curmin=min(val,self.minstack[-1])
            self.minstack.append(curmin)
    def pop(self):
        if self.mainstack:
            self.minstack.pop()
            self.mainstack.pop()
    def top(self):
         if self.mainstack:
            return self.mainstack[-1]
         else:
             return None
    def getMin(self):
        if self.mainstack:
            return self.minstack[-1]
        else:
            return None
