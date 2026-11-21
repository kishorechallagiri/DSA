class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = j = 0
        sumval = 0
        count = 0
        mincount = float('inf')
        minval = float('inf')
        while j < len(nums) :
            sumval += nums[j]
            count += 1
            while sumval >= target:
                minval = min(sumval,minval)
                mincount = min(mincount,count)
                sumval -= nums[i]
                count -= 1
                i += 1
            j += 1
        return mincount if mincount != float('inf') else 0                