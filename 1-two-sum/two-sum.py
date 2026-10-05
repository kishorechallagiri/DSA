class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hash and hash[val] != i:
                return [i,hash[val]]
              