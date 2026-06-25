class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        lst=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    lst.append(arr1[j])
        remaining=[]           
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                remaining.append(arr1[i])
        remaining.sort()  
        lst.extend(remaining) 
        return lst    
                   

        







        