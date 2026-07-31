class Solution(object):
    def nextGreaterElements(self, nums):
        nums = nums*2
        n=len(nums)
        arr=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while len(stack) and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack):
                arr[i]=stack[-1]  
            stack.append(nums[i]) 
        return arr[:n/2]  


        
        

        