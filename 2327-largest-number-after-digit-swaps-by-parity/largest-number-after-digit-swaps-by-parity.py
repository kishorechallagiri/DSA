class Solution(object):
    def largestInteger(self, num):
        lst1 = []
        lst2 = []
        for ch in str(num):
            if int(ch)%2 == 1:
                lst2.append(ch)
            else:
                lst1.append(ch)   
        lst1 = sorted(lst1,reverse = True) 
        lst2 = sorted(lst2,reverse = True) 
        
        strg = ""
        i=j=0
        k = 0
        while k < len(str(num)):
            if int(str(num)[k]) % 2 == 0:
                strg += lst1[i] 
                i+=1
            else:
                strg += lst2[j] 
                j+=1
            k+=1
        return int(strg)          
                
        