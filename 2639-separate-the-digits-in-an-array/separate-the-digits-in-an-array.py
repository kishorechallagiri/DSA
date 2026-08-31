class Solution(object):
    def separateDigits(self, nums):
        lst=[]
        result = ''.join(map(str, nums))
        for ch in result:
            lst.append(int(ch))
        return lst   
        