class Solution(object):
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - k
        while l < r:
            m = l + (r - l) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]

        

        



        
    
       
        