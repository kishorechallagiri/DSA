class Solution(object):
    def numberOfSpecialChars(self, word):
        hash=set(word)
        count=0
        hash2=set()
        for ch in word:
            if ch.islower() and ch.upper() in hash:
                if ch not in hash2 and ch.upper() not in hash2:
                    hash2.add(ch)   
                    hash2.add(ch.upper())
                    count+=1
            elif ch.isupper() and ch.lower() in hash:
                if ch not in hash2 and ch.lower() not in hash2:
                    hash2.add(ch)
                    hash2.add(ch.lower())  
                    count+=1
        return count                



        