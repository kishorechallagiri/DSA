class Solution(object):
    def reverseWords(self, s):
        
        result = " ".join(s.split()[::-1])
        return str(result)
      
       
        
        
        
        