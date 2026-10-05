class Solution(object):
    def isSubsequence(self, s, t):
        newstrg = ""
        i = j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                newstrg += t[i]
                i += 1
                j +=1
            else:
                i+=1
        print(newstrg)        
        return newstrg == s        

        