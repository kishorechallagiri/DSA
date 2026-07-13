class Solution(object):
    def addToArrayForm(self, num, k):
        result = int("".join(map(str, num)))
        digit=result+k
        arr = list(map(int, str(digit)))

        return arr

        
       

         