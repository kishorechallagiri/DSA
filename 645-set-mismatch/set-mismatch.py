class Solution(object):
    def findErrorNums(self, nums):
        freq = {}
        n = len(nums)
        lst = []

        for ch in nums:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        for ch in nums:
            if freq[ch] == 2:
                lst.append(ch)
                break

        hashset = set(nums)

        for i in range(1, n + 1):
            if i not in hashset:
                lst.append(i)
                break

        return lst  