class Solution(object):
    def countDigits(self, num):
        s=str(num)
        count=0
        for i in range(len(s)):
            if num%(int(s[i]))==0:
                count+=1
        return count        
            
     

        
        