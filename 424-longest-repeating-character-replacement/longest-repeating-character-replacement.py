
class Solution(object):
    def characterReplacement(self, s, k):
        i = j = 0
        map = {}
        maxWindow = 0
        while j < len(s):
            if s[j] not in map:
                map[s[j]] = 0
            map[s[j]] += 1

            if self.isWindowValid(map, k):
                maxWindow = max(maxWindow, j - i + 1)
                j += 1
            else:
                map[s[i]] -= 1
                i += 1
                j += 1

        return maxWindow

    def isWindowValid(self, map, k):
        totalcount = 0
        maxcount = 0

        for i in range(26):
            char = chr(i + 65)
            if char in map:
                totalcount += map[char]
                maxcount = max(maxcount, map[char])

        return totalcount - maxcount <= k
