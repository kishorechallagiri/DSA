class Solution(object):
    def largestInteger(self, nums, k):
        maxval = float('-inf')
        hash = {}
        for i in range(len(nums) - k + 1):
            subarr = set(nums[i:i+k])
            for ch in subarr:
                if ch not in hash:
                    hash[ch] = 1
                else:
                    hash[ch] += 1
        for ch in hash:
            if hash[ch] == 1:
                if ch > maxval :
                    maxval = ch 
        return maxval if maxval!=float('-inf') else -1  