class Solution(object):
    def lengthOfLastWord(self, s):
        n=len(s)-1
        while(n>=0):
            if s[n]!=" ":
                
                break
            n-=1    
        count=0
        while(n>=0):
            if s[n]!=" ":
                count+=1
                n-=1
            else:
                break  
        return count          

        