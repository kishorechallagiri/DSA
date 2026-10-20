from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        hash={}
        
        x = 0
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
                nums[x] = nums[i]
                x += 1
            else:
                hash[nums[i]] += 1
                if hash[nums[i]] < 3:
                    nums[x] = nums[i]
                    x += 1
        return x


        

        


        















      