class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        arr=[-1]*n
        stack=[]
        stack.append(arr[n-1])
        for i in range(2 * n - 2, -1, -1):
            while stack:
                top=stack[len(stack)-1]
                if nums[i%n]<top:
                    arr[i%n]=top
                    break
                else:
                    stack.pop()
            stack.append(nums[i%n])
        return arr[0:n]            