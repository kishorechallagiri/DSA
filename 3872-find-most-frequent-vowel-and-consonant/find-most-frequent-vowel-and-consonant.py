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
        for ch in s:
            if ch in vowel:
                maxvowel=max(maxvowel,map[ch])
            else:
                maxconsonant=max(maxconsonant,map[ch]) 
        return maxvowel+maxconsonant           

       
        