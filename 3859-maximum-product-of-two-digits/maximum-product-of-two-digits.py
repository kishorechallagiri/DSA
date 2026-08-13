class Solution(object):
    def maxProduct(self, n):
        s=str(n)
        maxproduct=0
        for i in range(len(s)):
            
            for j in range(i+1,len(s)):
                if int(s[i])*int(s[j])>maxproduct:
                    maxproduct=max(maxproduct,int(s[i])*int(s[j]))
        return maxproduct            


        