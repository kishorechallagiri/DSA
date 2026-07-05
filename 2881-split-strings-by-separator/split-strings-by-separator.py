class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        new=[]
        for i in words:
            word=""
            for ch in i:
                if ch!=separator:
                    word+=ch
                else:
                    if word:
                        new.append(word)
                        word=""
            if word:
                new.append(word)

        return new
        

        