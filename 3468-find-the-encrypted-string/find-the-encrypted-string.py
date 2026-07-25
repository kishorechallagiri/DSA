class Solution(object):
    def getEncryptedString(self, s, k):
        newstr=""
        for i in range(len(s)):
            newstr+= s[(i+k) % len(s)]
        return newstr    
       
        
        