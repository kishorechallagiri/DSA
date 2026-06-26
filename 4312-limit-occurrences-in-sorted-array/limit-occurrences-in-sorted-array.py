class Solution(object):
    def limitOccurrences(self, nums, k):
        
        lst = []
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0

            if count[num] < k:
                lst.append(num)
                count[num] += 1

        return lst








        