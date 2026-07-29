
class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                b=stack.pop()    
                a=stack.pop()  
                if tokens[i]=="+":
                    stack.append(a+b)
                elif tokens[i]=="-":
                    stack.append(a-b)  
                elif tokens[i]=="*":
                    stack.append(a*b) 
                elif tokens[i]=="/":
                    stack.append(int(float(a)/b))         
        return stack.pop()        

        