class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        mp={}
        stack=[]
        n=len(nums2)
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            mp[nums2[i]]=stack[-1] if stack else -1
            stack.append(nums2[i])   
        return [mp[x] for x in nums1]    
        