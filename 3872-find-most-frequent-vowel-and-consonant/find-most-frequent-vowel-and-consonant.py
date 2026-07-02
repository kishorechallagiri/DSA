class Solution(object):
    def maxFreqSum(self, s):
        map={}
           
        for ch in s:
            if ch not in map:
                map[ch] = 1
            else:
                map[ch] += 1
        vowel=["a","e","i","o","u"]  
        maxvowel=0
        maxconsonant=0
        for i in range(len(s)):
            if s[i] in vowel:
                if map[s[i]]>maxvowel:
                    maxvowel=map[s[i]]    
            else:
                if map[s[i]]>maxconsonant:
                    maxconsonant=map[s[i]]
        return maxvowel+maxconsonant            

       
        