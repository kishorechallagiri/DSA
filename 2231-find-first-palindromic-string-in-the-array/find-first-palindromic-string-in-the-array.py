class Solution(object):
    def firstPalindrome(self, words):
        strg=""
        for i in range(len(words)):
            for j in range(len(words[i])-1,-1,-1):
                strg+=words[i][j]
            if strg==words[i]:
                return strg
            else:
                strg=""   
        return strg             
                
        