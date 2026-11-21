class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = j = 0
        sumval = 0
        mincount = float('inf')

        while j < len(nums):
            sumval += nums[j]

            while sumval >= target:
                mincount = min(mincount, j - i + 1)
                sumval -= nums[i]
                i += 1

            j += 1

        return mincount if mincount != float('inf') else 0