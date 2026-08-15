class Solution(object):
    def reverse(self, x):
        n=abs(x)
        s=str(n)
        rev=s[::-1]
        rev=int(rev)
        if rev > 2**31 - 1:
            return 0
        return -rev if x < 0 else rev
