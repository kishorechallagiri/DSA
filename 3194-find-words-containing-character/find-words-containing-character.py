class Solution(object):
    def findWordsContaining(self, words, x):
        lst=[]
        for i in range(len(words)):
            for  j in range(len(words[i])):
                if words[i][j]==x:
                    lst.append(i)
                    break
        return lst            
       