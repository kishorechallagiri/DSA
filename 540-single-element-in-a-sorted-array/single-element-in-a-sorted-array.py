class Solution(object):
    def singleNonDuplicate(self, arr):
        l = 0
        r = len(arr) - 1
        while l <r:
            m = l + (r - l)/2
            #pair is left
            if arr[m] == arr[m-1]:
                leftcount = m-1-l
                if leftcount%2 == 1:
                    r = m - 2
                else:
                    l = m + 1
            #pair is right        
            elif arr[m] == arr[m+1]:
                leftcount = m-l
                if leftcount%2 == 1:
                    r = m -1
                else:
                    l = m+2
            else:
                return arr[m]       
        return arr[l]                     

