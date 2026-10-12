class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxWS = 0
        i = 0
        map = {}
        for j in range(len(s)):
            if s[j] in map and map[s[j]] >= i:
                i = map[s[j]] + 1
            map[s[j]] = j
            currWS = j - i + 1
            maxWS = max(currWS,maxWS)   
        return maxWS    
                

        
        