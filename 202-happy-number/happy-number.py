class Solution(object):
    def isHappy(self, n,hash=None):
        if hash is None:
            hash = set()
        if n == 1:
            return True
        if n in hash:
            return False
        hash.add(n)
        num = str(n)
        total = 0
        for ch in num:
            total += int(ch) ** 2

        return self.isHappy(total, hash)