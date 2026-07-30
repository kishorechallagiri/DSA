class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return ans
            
                
        