class Solution(object):
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Try removing s[l]
                left = l + 1
                right = r
                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                if left >= right:
                    return True

                # Try removing s[r]
                left = l
                right = r - 1

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                if left >= right:
                    return True

                return False

        return True
                 


                
         


        