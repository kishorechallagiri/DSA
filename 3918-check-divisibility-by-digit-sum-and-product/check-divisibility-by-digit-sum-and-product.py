class Solution(object):
    def checkDivisibility(self, n):
        val=0
        mul=1
        for ch in str(n):
            val+=int(ch)
            mul*=int(ch)
        sumval=val+mul
        return  n%sumval==0    
        