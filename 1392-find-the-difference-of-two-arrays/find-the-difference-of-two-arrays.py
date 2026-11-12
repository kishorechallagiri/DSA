class Solution(object):
    def findDifference(self, nums1, nums2):
        hashset = set(nums2)
        ans1 = []
        for ch in nums1:
            if ch not in hashset:
                if ch not in ans1:
                    ans1.append(ch) 
        hashset2 = set(nums1)
        ans2 = []
        for ch in nums2:
            if ch not in hashset2:
                if ch not in ans2:
                    ans2.append(ch)
        return [ans1,ans2]                  

      