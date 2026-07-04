class Solution(object):
    def isPalindrome(self, s):
        lst=""
        for ch in s:
            if ch.isalnum():
                lst+=ch.lower()

        return lst==lst[::-1]              




     

    


        
        