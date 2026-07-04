class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)

        for start in range(0, len(s), 2 * k):
            n = min(k, len(s) - start)

            for j in range(n // 2):
                s[start + j], s[start + n - 1 - j] = (
                    s[start + n - 1 - j],
                    s[start + j],
                )

        return "".join(s)
