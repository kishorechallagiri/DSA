class Solution(object):

    def findIntersectionValues(self, nums1, nums2):
        count1 = sum(1 for x in nums1 if x in nums2)
        count2 = sum(1 for x in nums2 if x in nums1)
        return [count1, count2]

            

        