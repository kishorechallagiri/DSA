class Solution(object):
    def countCommas(self, n):
        if len(str(n))<4:
            return 0
        count = 0    
        while len(str(n))>3:
            count+=1
            n-=1
            
        return count    