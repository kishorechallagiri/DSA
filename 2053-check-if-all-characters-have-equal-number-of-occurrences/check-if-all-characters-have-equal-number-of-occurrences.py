class Solution(object):
    def areOccurrencesEqual(self, s):
        hash={}
        for ch in s:
            if ch not in hash:
                hash[ch]=1
            else:
                hash[ch]+=1
        counts = list(hash.values())

        for i in range(len(counts) - 1):
            if counts[i] != counts[i + 1]:
                return False

        return True