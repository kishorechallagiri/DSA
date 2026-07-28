class Solution(object):
    def mergeAlternately(self, word1, word2):
        strg=""
    
        left=0
        right=0
        while left<len(word1) or right<len(word2):
            strg += (word1[left] if left< len(word1) else "") + (word2[right] if left < len(word2) else "")
            left+=1
            right+=1
        return strg     
            
        