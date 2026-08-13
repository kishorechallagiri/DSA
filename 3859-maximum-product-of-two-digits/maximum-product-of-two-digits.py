class Solution(object):
    def maxProduct(self, n):
        s=str(n)
        first=second=0
        for ch in s:
            if int(ch)>first:
                second=first
                first=int(ch)
            elif int(ch)>second:
                second=int(ch)    

            
        return first*second          


        