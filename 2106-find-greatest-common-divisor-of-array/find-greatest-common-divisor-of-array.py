class Solution(object):
    def findGCD(self, nums):
        largest = max(nums)
        smallest = min(nums)
        lst1 = []
        for i in range(1,largest+1):
            if largest % i == 0:
                lst1.append(i)
        gcd = float('-inf')        
        for j in range(1,smallest+1):
            if smallest % j == 0:
                if j in lst1:
                    if j > gcd:
                        gcd = j
        return gcd                

        


        