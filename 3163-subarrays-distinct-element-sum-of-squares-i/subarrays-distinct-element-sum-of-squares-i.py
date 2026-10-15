class Solution(object):
    def sumCounts(self, arr):
        lst = []
        n = len(arr)
        for i in range(n):
            for j in range(i, n):
                lst.append(len(set(arr[i:j + 1])))
        sumval = 0
        for ch in lst:
            sumval += ch*ch
        return sumval