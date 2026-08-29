class Solution(object):
    def clearDigits(self, s):
        arr = []

        for ch in s:
            if ch.isdigit():
                arr.pop()
            else:
                arr.append(ch)

        return ''.join(arr)
        