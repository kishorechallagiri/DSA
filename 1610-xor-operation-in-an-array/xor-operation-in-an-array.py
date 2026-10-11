class Solution(object):
    def xorOperation(self, n, start):
        arr = [0]*n
        for i in range(n):
            arr[i] = start + 2*i
        xor = 0
        for num in arr:
            xor ^= num
        return xor    