class Solution(object):
    def minAddToMakeValid(self, s):
        balance = 0
        additions = 0

        for char in s:
            if char == "(":
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1

        return additions + balance