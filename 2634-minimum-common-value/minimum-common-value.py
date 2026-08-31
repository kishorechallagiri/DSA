class Solution(object):
    def getCommon(self, nums1, nums2):
        hash=set(nums1)
        for ch in nums2:
            if ch in hash:
                return ch
        return -1

        
        