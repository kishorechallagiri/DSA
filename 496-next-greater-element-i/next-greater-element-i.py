class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ngeMap={}
        stack=[]
        n=len(nums2)
        stack.append(nums2[n-1])
        ngeMap[nums2[n-1]]=-1
        for i in range(n-2,-1,-1):
            top=stack[-1]
            if nums2[i]<top:
                ngeMap[nums2[i]]=top
            else:
                while stack:
                    if stack[-1]<nums2[i]:
                        stack.pop()
                    else:
                        ngeMap[nums2[i]]=stack[-1]
                        break
                if not stack:
                    ngeMap[nums2[i]] = -1        
            stack.append(nums2[i])    
        ans=[]                    
        for i in range(len(nums1)):
            ans.append(ngeMap[nums1[i]])
            
       
        return ans     
            
              
        