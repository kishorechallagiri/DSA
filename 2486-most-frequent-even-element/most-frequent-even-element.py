class Solution(object):

    def mostFrequentEven(self, nums):

        hash = {}

        for ch in nums:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1

        max_freq = 0
        ans = float('inf')

        for num in hash:
            if num % 2 == 0:
                if hash[num] > max_freq:
                    max_freq = hash[num]
                    ans = num
                elif hash[num] == max_freq:
                    ans = min(ans, num)

        if ans != float('inf'):
            return ans
        else:
            return -1

        