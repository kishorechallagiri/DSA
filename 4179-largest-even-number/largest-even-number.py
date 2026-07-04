class Solution(object):
    def largestEven(self, s):
        n=len(s)-1
        while n>=0:
            if int(s[n])%2==0:
                return s[:n+1]
            n-=1
        return ""        