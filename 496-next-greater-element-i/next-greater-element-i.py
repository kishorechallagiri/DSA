class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ngeMap={}
        stack=[]
        n=len(nums2)
        for i in range(n-1,-1,-1):
                while stack and stack[-1]<nums2[i]:
                    stack.pop()
                if not stack:
                    ngeMap[nums2[i]] = -1
                else:
                    ngeMap[nums2[i]] = stack[-1]        
                stack.append(nums2[i])    
        ans=[]                    
        for i in range(len(nums1)):
            ans.append(ngeMap[nums1[i]])
            
        return ans     
            
              
        