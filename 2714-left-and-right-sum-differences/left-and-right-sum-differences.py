class Solution(object):
    def leftRightDifference(self, nums):
        lst = []

        for l in range(len(nums)):
            leftsum = 0
            rightsum = 0

            # left side
            for i in range(0, l):
                leftsum += nums[i]

            # right side
            for i in range(l + 1, len(nums)):
                rightsum += nums[i]

            lst.append(abs(leftsum - rightsum))

        return lst

                






        
        