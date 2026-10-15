class Solution(object):
    def trailingZeroes(self, n):
        fact = 1

        for i in range(1, n + 1):
            fact *= i

        s = str(fact)
        count = 0

        for ch in s[::-1]:
            if ch == '0':
                count += 1
            else:
                break

        return count