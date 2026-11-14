class Solution(object):
    def minimumSumSubarray(self, arr, l, r):
        arrval = []

        for k in range(l, r + 1):
            for i in range(len(arr) - k + 1):
                total = sum(arr[i:i+k])

                if total > 0:
                    arrval.append(total)

        if arrval:
            return min(arrval)
        return -1


        