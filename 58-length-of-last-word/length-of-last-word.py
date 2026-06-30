class Solution(object):
    def lengthOfLastWord(self, s):
        n=len(s)-1
        count=0
        while n>=0:
            if s[n]!=" ":
                count+=1
            elif count>0:
                break
            n-=1
        return count            
        
        