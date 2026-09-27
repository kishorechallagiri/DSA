class Solution(object):
    def isValid(self, s):
        stack=[]
        map={
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        for i in range(len(s)):
            if s[i] in map:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top=stack.pop()
                if not top or s[i]!=map[top]:
                    return False
        return len(stack) == 0              
        

       