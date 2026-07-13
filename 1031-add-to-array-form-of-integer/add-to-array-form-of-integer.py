class Solution(object):
    def addToArrayForm(self, num, k):
        strg=""
        for i in range(len(num)):
            strg+=str(num[i])
        digit=int(strg)+k
        lst=[]
        for i in str(digit):
            lst.append(int(i))   
        return lst     


         