class Solution(object):
    def numDifferentIntegers(self, word):
        strg=""
        for ch in word:
            if ch.isalpha():
                strg+=" "
            elif ch.isdigit():
                strg+=ch
        print(strg)        
        lst=[]  
        num=""
        count=0
        for i in range(len(strg)):
            if  strg[i].isdigit():
                num+=strg[i]
            else: 
                if num:
                    number=int(num)
                    if number not in lst:
                        lst.append(number)
                        count+=1
                    num=""
        if num:
            number = int(num)
            if number not in lst:
                count += 1
                
                
        return count            

        