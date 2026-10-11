class Solution(object):
    def rearrangeArray(self, nums):
        i = 0
        x = 0
        lst = [0]*len(nums)
        while i <len(nums):
            k = i
            if nums[i]>0:
                lst[x] = nums[i]
                x+=2
                i = k+1
            else:
                i+=1     
        j = 0
        y = 1
        while j<len(nums):
            val = j
            if nums[j]<0:
                lst[y]=nums[j]
                y+=2
                j = val+1
            else:
                j+=1
            
        return lst                    

        