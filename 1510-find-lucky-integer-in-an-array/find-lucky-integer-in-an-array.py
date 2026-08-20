class Solution(object):
    def findLucky(self, arr):
        hash={}
        for ch in arr:
            if ch not in hash:
                hash[ch]=1
            else:
                hash[ch]+=1
        largest=-1      
        for ch in arr:
            if ch==hash[ch] :
                if ch>largest:
                    largest=ch

        return largest                  
        