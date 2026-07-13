class Solution(object):
    def addDigits(self, num):
        if 0 <= num <= 9:
            return num
        strg=str(num)
        count=0
        for i in strg:
            count+=int(i)
        return self.addDigits(count)    




   

        