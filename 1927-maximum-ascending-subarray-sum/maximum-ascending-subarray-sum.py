class Solution(object):
    def maxAscendingSum(self, arr):
        n = len(arr)
        lst = []
        maxval = float('-inf')
        for i in range(n):
            for j in range(i, n):
                subarray = arr[i:j + 1]
                inc = 1
                for k in range(1,len(subarray)):
                    if subarray[k] > subarray[k-1]:
                        inc = 1
                    else:
                        inc = 0
                        break

                if inc == 1:
                    maxval = max(maxval,sum(subarray))

        return maxval