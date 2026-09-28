class Solution(object):
    def checkIfPangram(self, sentence):
        letters = set()
        for ch in sentence:
            letters.add(ch)
        for ch in range(ord('a'), ord('z') + 1):
            if chr(ch) not in letters:
                return False
        return True        
        