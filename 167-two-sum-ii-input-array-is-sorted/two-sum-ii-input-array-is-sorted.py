class Solution(object):
    def twoSum(self, nums, target):
        i ,j = 0, len(nums) - 1
        while i < j:
            val = nums[i] + nums[j]
            if val == target:
                return [ i+1, j+1]
            elif val > target:
                j-=1
            elif val<target:
                i += 1
