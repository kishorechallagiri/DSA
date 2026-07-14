class Solution(object):
    def reverse(self, x):
        n=abs(x)
        reversed=0
        while n>0:
            last=n%10
            reversed=reversed*10+last
            n//=10
        if reversed > 2**31 - 1:
            return 0
        return -reversed if x < 0 else reversed    
               
 
       