class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i+1
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hash and hash[val] != i+1:  
                return [i+1,hash[val]]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        