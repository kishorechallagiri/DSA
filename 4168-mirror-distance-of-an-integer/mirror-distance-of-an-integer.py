class Solution(object):
    def mirrorDistance(self, n):
        new=""
        s=str(n)
        for i in range(len(s)-1,-1,-1):
            new+=s[i]
        return abs(n-int(new))    
        
        