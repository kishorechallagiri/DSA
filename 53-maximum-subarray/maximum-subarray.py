class Solution(object):
    def maxSubArray(self, arr):
        maxval = float('-inf')
        sumval = 0
        for ch in arr:
            sumval += ch
            if sumval > maxval :
                maxval = sumval
            if sumval < 0 :
                sumval = 0
        return maxval            

        