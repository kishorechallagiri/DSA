class Solution(object):
    def maxAlternatingSum(self, arr):
        arr.sort(key = abs)

        result = []
        left = 0
        right = len(arr) - 1

        while left <= right:
            result.append(arr[right])  # Largest remaining element
            right -= 1

            if left <= right:
                result.append(arr[left])  # Smallest remaining element
                left += 1
        sumval = 0

        for i in range(len(result)):
            if i % 2 == 0:
                sumval += result[i] * result[i]
            else:
                sumval -= result[i] * result[i]

        return sumval
