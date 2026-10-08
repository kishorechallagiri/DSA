class Solution(object):
    def removeOuterParentheses(self, s):
        stack=0
        ans=""
        for i in range(len(s)):
            if s[i]=="(":
                stack+=1
                if stack>1:
                    ans+=s[i]
            else:
                
                if stack>1:
                    ans+=s[i]
                stack-=1           
        return ans         
            