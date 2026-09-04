class Solution(object):
    def stableMountains(self, height, threshold):
        lst=[]
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                lst.append(i)
        return lst        