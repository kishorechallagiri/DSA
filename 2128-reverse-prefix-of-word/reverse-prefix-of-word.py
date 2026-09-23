class Solution(object):
    def reversePrefix(self, word, ch):
        reverse = ""
        for i in range(len(word)):
            if word[i] == ch:
                val = word[:i+1]
                reverse = val[::-1] + word[i+1:]
                return reverse
        if not reverse:
            return word         

        