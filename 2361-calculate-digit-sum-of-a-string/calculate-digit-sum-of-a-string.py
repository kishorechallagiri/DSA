class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            lst = []

            for i in range(0, len(s), k):
                group = s[i:i+k]

                total = 0
                for ch in group:
                    total += int(ch)

                lst.append(str(total))

            s = "".join(lst)

        return s

            
            


        


        