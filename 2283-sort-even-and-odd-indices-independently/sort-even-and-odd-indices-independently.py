class Solution(object):
    def sortEvenOdd(self, nums):
        even=[]
        odd=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])    
        odd=sorted(odd,reverse=True)
        even=sorted(even)
        p=0
        q=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even[p]
                p+=1
            else:
                nums[i]=odd[q]  
                q+=1
        return nums          

         


        