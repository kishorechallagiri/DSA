class Solution(object):
    def prefixCount(self, words, pref):
        l = len(pref)
        count = 0
        for i in range(len(words)):
            val = words[i]
            if val[:l] == pref:
                count += 1
        return count        
        