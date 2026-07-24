class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        lst=[]
        for ch in s:
            lst.append(ch[::-1])
        return " ".join(lst)

        