class Solution(object):
    def canPlaceFlowers(self,nums, n):
        if n == 0:
            return True
        first = 0
        last = -1   
        #one lement
        if len(nums) == 1:
            if nums[0] == 0:
                nums[0] == 1
                return True
            else:
                return False     
        for i in range(len(nums)-1):
            #FIRST ELEMENT TO CHECK
            if  nums[first] == 0  and  nums[first+1] == 0:
                if n:
                    nums[first] = 1
                    n-=1   
                else:
                    return True
             
            if nums[i] == 0 and nums[i-1] == 0 and nums[i+1] == 0:
                if n:
                    nums[i] = 1
                    n-=1   
                else:
                    return True
            #for last element      
            if nums[last] == 0 and nums[last-1] == 0:
                if n:
                    nums[last] = 1
                    n-=1   
                else:
                    return True         
            if n == 0:
                return True
        
        return False            
            
        
            



        