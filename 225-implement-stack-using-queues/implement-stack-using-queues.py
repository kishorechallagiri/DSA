from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        

    def push(self, x):
        self.q1.append(x)
        

    def pop(self):
        n=len(self.q1)
        for i in range(n-1):
            self.q2.append(self.q1.popleft())
        ans=self.q1.popleft()
        self.q1,self.q2=self.q2,self.q1
        return ans    

        
        

    def top(self):
        n=len(self.q1)
        for i in range(n-1):
            self.q2.append(self.q1.popleft())
        front=self.q1.popleft()
        self.q2.append(front)  
        self.q1,self.q2=self.q2,self.q1
        return front

    def empty(self):
        return len(self.q1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()