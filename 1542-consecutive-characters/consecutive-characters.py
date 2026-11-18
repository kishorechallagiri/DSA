class Solution(object):
    def maxPower(self, s):
        count = 1 
        maxcount = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            maxcount = max(count,maxcount)   
        return maxcount         


