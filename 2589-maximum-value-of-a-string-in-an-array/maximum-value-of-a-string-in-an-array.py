class Solution(object):
    def maximumValue(self, strs):
        mincount=0
        maxcount=0

        for i in range(len(strs)):
            if strs[i].isdigit():
                mincount+=int(strs[i])
            else:
                mincount+=len(strs[i])  
            maxcount=max(mincount,maxcount)  
            mincount=0
        return  max(mincount,maxcount)         
         
        