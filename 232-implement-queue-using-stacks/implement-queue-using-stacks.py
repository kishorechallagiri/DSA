class MyQueue(object):

    def __init__(self):
        self.q1=[]
        self.q2=[]
        

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if len(self.q2)==0:
            while len(self.q1):
                self.q2.append(self.q1.pop())
        return self.q2.pop()    

    def peek(self):
        if len(self.q2)==0:
            while len(self.q1):
                self.q2.append(self.q1.pop())
        return self.q2[len(self.q2)-1]

       
        

    def empty(self):
        return len(self.q1)==0 and len(self.q2)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()