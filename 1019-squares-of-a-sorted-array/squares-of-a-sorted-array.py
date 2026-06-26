class Solution(object):
    def sortedSquares(self, nums):
        lst=[]
        for i in range(len(nums)):
            lst.append(nums[i]**2)
        lst.sort() 
        return lst   

        