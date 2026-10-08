class Solution(object):
    def maxArea(self, arr):
        maxval = float('-inf')
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i]<arr[j]:
                area = arr[i]*(j - i)
                maxval = max(maxval,area)
                i+=1
            elif arr[i]>arr[j]:
                area = arr[j]*(j - i)
                maxval = max(maxval,area)
                j-=1
            elif arr[i] == arr[j]:
                area = arr[i]*(j - i)
                maxval = max(maxval,area)
                i+=1
        return maxval                   