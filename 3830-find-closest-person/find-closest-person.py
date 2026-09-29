class Solution(object):
    def findClosest(self, x, y, z):
        val1 = abs(z - x)
        val2 = abs(z - y)
        if val1 < val2 :
            return 1
        elif val2 < val1:
            return 2
        else:
            return 0        
        