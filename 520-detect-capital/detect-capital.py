class Solution(object):
    def detectCapitalUse(self, word):
        return word.upper()==word or word.title()==word or word.lower()==word