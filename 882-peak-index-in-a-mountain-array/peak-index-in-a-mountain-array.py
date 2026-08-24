class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l,r=0,len(arr)-1
        while l<=r:
            m=l+(r-l)//2
            if arr[m]>arr[m-1] and arr[m]>arr[m+1]:
                return m
            if arr[m]<arr[m-1]:
                r=m
                
            else:
                l=m+1
                  
              

        