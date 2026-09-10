class Solution(object):
    def intersection(self, nums1, nums2):
        hash = set(nums1)
        lst = []
        for ch in nums2:
            if ch in hash:
                if ch not in lst:
                    lst.append(ch)
        return   lst          

     
        