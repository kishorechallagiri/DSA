class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            # Calculate digit product of current n
            product = 1
            for digit in str(n):
                product *= int(digit)
            
            # Check divisibility condition
            if product % t == 0:
                return n
            
            n += 1
  




        