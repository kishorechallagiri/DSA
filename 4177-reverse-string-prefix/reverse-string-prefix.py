class Solution(object):
    def reversePrefix(self, s, k):
        reversal = ""
        for i in range(len(s)):
            if i == k - 1:
                val = s[:i+1] 
                reversal = val[::-1] + s[i+1:]
                return reversal
