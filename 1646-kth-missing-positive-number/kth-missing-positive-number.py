class Solution(object):
    def findKthPositive(self, arr, k):
        lst=[]
        i=1
        hashset=set(arr)
        while len(lst)<k:
            if i not in hashset:
                lst.append(i)
            i+=1
        return lst[k-1]        

       