class Solution(object):
    def dominantIndex(self, nums):
        maxval = max(nums)
        val = []
        for i in range(len(nums)):
            if nums[i]!=maxval:
                if maxval < nums[i]*2:
                    return -1
                else:
                    continue
            else:
                val.append(i)
                continue
        return sum(val)        



       
        