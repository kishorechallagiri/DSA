class Solution(object):
    def sortArrayByParity(self, nums):
        x = 0
        lst = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                lst[x] = nums[i]
                x += 1
        for j in range(len(nums)):
            if nums[j]%2 == 1:
                lst[x] = nums[j]
                x += 1
        return lst       