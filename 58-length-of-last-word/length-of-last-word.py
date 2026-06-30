class Solution(object):
    def lengthOfLastWord(self, s):
        lst1=list(map(str,s.split()))
        for i in range(len(lst1)):
            return len(lst1[-1])
        
        
        
        
  
        