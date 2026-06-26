class Solution(object):
    def majorityElement(self, nums):
        count={}
   
        for num in nums:
            if num not in count:
                count[num] = 1      
            else:
                count[num] += 1
    
               
        return max(count,key=count.get)        





        