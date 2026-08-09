class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hash={}
        for ch in magazine:
            if ch not in hash:
                hash[ch]=1
            else:
                hash[ch]+=1
        for char in ransomNote:
            if char not in hash or hash[char] == 0:
                return False
            else:
                hash[char] -= 1
        return True            
                    
            
        