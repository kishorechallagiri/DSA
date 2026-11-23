class Solution(object):
    def judgeSquareSum(self, c):
        l = 0
        r = int(c**0.5)

        while l <= r:
            sq = l**2 + r**2

            if sq == c:
                return True

            elif sq > c:
                r -= 1

            else:
                l += 1

        return False