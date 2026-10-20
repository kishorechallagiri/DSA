class Solution(object):
    def removeDuplicates(self, nums):
        x = 0

        for num in nums:
            if x < 2 or num != nums[x - 2]:
                nums[x] = num
                x += 1

        return x


        

        


        















      