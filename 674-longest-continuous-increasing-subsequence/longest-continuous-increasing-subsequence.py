class Solution(object):
    def findLengthOfLCIS(self, arr):
        maxval = 1
        count = 1
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                count += 1
            else:
                count = 1
            maxval = max(maxval,count) 
        return maxval           