class Solution(object):
    def reverseWords(self, s):
        lst1=list(map(str,s.split()))
        result = " ".join(s.split()[::-1])
        return str(result)
      
       
        
        
        
        