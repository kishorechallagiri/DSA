class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if jewels[j]==stones[i]:
                    count+=1
                    break
            
        return count        




        