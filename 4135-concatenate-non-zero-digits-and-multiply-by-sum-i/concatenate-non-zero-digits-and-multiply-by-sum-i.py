class Solution(object):
    def sumAndMultiply(self, n):
        strg=""
        count=0
        for ch in str(n):
            if int(ch)!=0:
                count+=int(ch)
                strg+=str(ch)
        if strg == "":
            return 0
        
        v=int(strg) 
        return v*count  


        