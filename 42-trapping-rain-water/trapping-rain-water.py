class Solution(object):
    def trap(self, arr):
        n = len(arr)
        maxL = [0] * n
        maxL[0] = arr[0]
        for i in range(1,n):
            maxL[i] = max(arr[i],maxL[i-1])
        maxR = [0] * n
        maxR[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            maxR[i] = max(maxR[i+1],arr[i])
        ans = 0 
        for i in range(n):
            watertrapping = min(maxL[i],maxR[i]) - arr[i] 
            ans += watertrapping if watertrapping > 0 else 0
        return ans    
        