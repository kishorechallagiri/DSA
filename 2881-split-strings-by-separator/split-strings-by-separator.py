class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        result = []

        for word in words:
            for part in word.split(separator):
                if part:
                    result.append(part)

        return result


        