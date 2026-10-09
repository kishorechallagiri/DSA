
class Solution(object):
    def twoSum(self, arr, x, ans):
        i = x + 1
        j = len(arr) - 1

        while i < j:
            s = arr[i] + arr[j] + arr[x]

            if s > 0:
                j -= 1
            elif s < 0:
                i += 1
            else:
                ans.append([arr[x], arr[i], arr[j]])
                i += 1
                j -= 1

                while i < j and arr[i] == arr[i - 1]:
                    i += 1

    def threeSum(self, nums):
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.twoSum(nums, i, ans)

        return ans
