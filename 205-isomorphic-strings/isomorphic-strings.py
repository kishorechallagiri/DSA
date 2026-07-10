class Solution(object):
    def isIsomorphic(self, s, t):
        mapStoT={}
        mapTtoS={}
        for i in range(len(s)):
            if s[i] not in mapStoT and t[i] not in mapTtoS:
                mapStoT[s[i]]=t[i]
                mapTtoS[t[i]]=s[i]
            elif s[i] not in mapStoT or t[i] not in mapTtoS:
                return False    
            elif mapStoT[s[i]]!=t[i] or mapTtoS[t[i]]!=s[i] :
                return False
        return True          
        
        
        