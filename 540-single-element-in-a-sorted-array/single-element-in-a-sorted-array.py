class Solution(object):
    def singleNonDuplicate(self, nums):
        hash={}
        for ch in nums:
            if ch not in hash:
                hash[ch]=1
            else:
                hash[ch]+=1
        for ch in nums:
            if hash[ch]==1:
                return ch 

        """
        :type nums: List[int]
        :rtype: int
        """
        