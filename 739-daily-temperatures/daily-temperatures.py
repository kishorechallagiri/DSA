class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        stack=[]
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            ans[i]=stack[-1]-i if stack else 0
            stack.append(i)
        return ans        
        