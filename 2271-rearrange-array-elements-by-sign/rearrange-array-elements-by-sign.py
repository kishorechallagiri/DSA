class Solution(object):
    def rearrangeArray(self, nums):
        lst = [0] * len(nums)
        x = 0
        y = 1
        for num in nums:
            if num > 0:
                lst[x] = num
                x += 2
            else:
                lst[y] = num
                y += 2

        return lst             

        