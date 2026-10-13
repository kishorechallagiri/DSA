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
        left = 0
        right = left + 1

        while left < len(result):
            if right < len(result):
                sumval += (result[left] * result[left]) - (result[right] * result[right])
            else:
                sumval += result[left] * result[left]

            left += 2
            right = left + 1

        return sumval
