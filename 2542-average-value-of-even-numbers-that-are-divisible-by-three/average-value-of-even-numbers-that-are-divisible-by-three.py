class Solution(object):
    def averageValue(self, nums):
        lst=[]
        for i in range(len(nums)):
            if nums[i]%2==0 and nums[i]%3==0:
                lst.append(nums[i])
        if lst:
            return sum(lst) // len(lst)
        else:
            return 0    

                

        