class Solution(object):
    def longestMonotonicSubarray(self, arr):
        n = len(arr)

        inc = 1
        dec = 1
        maxval = 1

        for i in range(1, n):
            if arr[i] > arr[i-1]:
                inc += 1
                dec = 1

            elif arr[i] < arr[i-1]:
                dec += 1
                inc = 1

            else:
                inc = 1
                dec = 1

            maxval = max(maxval, inc, dec)

        return maxval