class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        hash=set()
        for i in range(len(jewels)):
            hash.add(jewels[i])
        for j in range(len(stones)) :
            if stones[j] in hash:
                count+=1   
             
              
        return count


   




        