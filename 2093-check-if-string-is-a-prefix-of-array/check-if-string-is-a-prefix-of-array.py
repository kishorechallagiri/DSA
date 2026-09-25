class Solution(object):
    def isPrefixString(self, s, words):
        strg = ""
        for i in range(len(words)):
            strg += words[i]
            if strg == s:
                return True
        return False        
            