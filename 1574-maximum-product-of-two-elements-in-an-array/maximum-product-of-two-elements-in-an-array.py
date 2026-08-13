class Solution(object):
    def maxProduct(self, nums):
        maxproduct=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if ((nums[i]-1)*(nums[j]-1))>maxproduct:
                    maxproduct=max(maxproduct,((nums[i]-1)*(nums[j]-1)))
        return maxproduct           


        