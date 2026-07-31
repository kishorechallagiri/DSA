class Solution(object):
    def firstUniqueEven(self, nums):
        hash_map = {}
        for num in nums:
            if num%2==0 :
                if num not in hash_map :
                    hash_map[num] = 1
                else:
                    hash_map[num] += 1
        for num in nums:
            if num % 2 == 0 and hash_map[num] == 1:
                    return num
        return -1
        