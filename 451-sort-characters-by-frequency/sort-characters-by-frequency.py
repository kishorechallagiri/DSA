class Solution(object):
    def frequencySort(self, s):
        hash = {}

        for ch in s:
            hash[ch] = hash.get(ch, 0) + 1

        result = sorted(hash.items(), key=lambda x: x[1], reverse=True)

        s1 = ""

        for key, value in result:
            s1 += key * value

        return s1