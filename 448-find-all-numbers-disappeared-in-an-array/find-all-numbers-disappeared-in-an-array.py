class Solution(object):
    def findDisappearedNumbers(self, nums):
        hashset=set()
        lst=[]
        for i in range(len(nums)):
            hashset.add(nums[i])
        for i in range(1,len(nums)+1)  :
            if i not in  hashset:
                lst.append(i)
        return lst        
                  


            
          
        
        