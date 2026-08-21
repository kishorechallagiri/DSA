class Solution(object):
    def search(self, arr, target):
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = l+(r - l)//2
            if arr[m] == target:
                return m
            #left sorted if it     
            if arr[l] <= arr[m]:
                if (target >= arr[l])  and (target < arr[m]):
                    r = m - 1
                else:
                    l = m + 1  
            else:
                if (target > arr[m]) and (target <= arr[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1                


        