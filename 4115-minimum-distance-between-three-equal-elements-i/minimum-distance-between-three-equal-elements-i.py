class Solution(object):
    def minimumDistance(self, nums):
        val=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k]:
                        ans= abs(i - j) + abs(j - k) + abs(k - i)
                        val=min(ans,val)

        return val  if val!=float('inf')  else -1         

        