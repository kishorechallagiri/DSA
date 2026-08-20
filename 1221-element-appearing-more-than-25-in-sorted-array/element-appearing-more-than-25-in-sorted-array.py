class Solution(object):
    def findSpecialInteger(self, arr):
        n=len(arr)
        hash={}
        for ch in arr:
            if ch not in hash:
                hash[ch]=1
            else:
                hash[ch]+=1
        for ch in arr:
            if hash[ch]>n//4:
                return ch        

        """
        :type arr: List[int]
        :rtype: int
        """
        