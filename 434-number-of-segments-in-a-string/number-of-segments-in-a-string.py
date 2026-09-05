class Solution(object):
    def countSegments(self, s):
        lst=[]
        count=0
        s=s.split()
        for ch in s:
            count+=1
        return count    
                
        