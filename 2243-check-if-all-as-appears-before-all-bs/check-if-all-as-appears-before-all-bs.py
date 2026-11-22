class Solution(object):
    def checkString(self, s):
        if len(s) == 0:
            return False
        if len(s) == 1:
            return True    
        if s[0] == "b":
            if s[1] == "a":
                return False    
        hash = {}
        for ch in s:
            if ch not in hash:
                hash[ch] = 1
                prev = ch    
            else:
                if ch in hash and ch!=prev:
                    return False
                if ch not in hash and ch!=prev:
                    return False    
                prev = ch    
                hash[ch] += 1
        return True                
        