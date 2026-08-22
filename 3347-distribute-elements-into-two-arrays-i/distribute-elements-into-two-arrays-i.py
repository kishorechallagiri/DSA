class Solution(object):
    def resultArray(self, nums):
        l=0
        r=1
        arr1=[]
        arr2=[]
        arr1.append(nums[l])
        arr2.append(nums[r])
        for i in range(r+1,len(nums)):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])  
        return arr1+arr2        
        

        
        

        
         


        
        