class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        newlist=[]
        for i in words:
            word=""
            for ch in i:
                if ch!=separator:
                    word+=ch
                else:
                    if word:
                        newlist.append(word)
                        word=""
            if word:
                newlist.append(word)

        return newlist
        

        