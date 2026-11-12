class Solution(object):
    def intersect(self, nums1, nums2):
        hash = {}
        for ch in nums1:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1
        ans = []        
        for ch in nums2:
            if ch in hash and hash[ch]!=0:
                ans.append(ch)
                hash[ch] -= 1
        return ans        
