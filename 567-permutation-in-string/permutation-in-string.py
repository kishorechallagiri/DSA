
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        hashS = [0] * 26
        hashW = [0] * 26

        window_length = len(s1)

        for i in range(window_length):
            hashS[ord(s1[i]) - ord('a')] += 1
            hashW[ord(s2[i]) - ord('a')] += 1

        i = 0
        j = window_length - 1

        while j < len(s2):
            if hashS == hashW:
                return True

            # Remove the character leaving the window
            hashW[ord(s2[i]) - ord('a')] -= 1

            i += 1
            j += 1

            # Add the character entering the window
            if j < len(s2):
                hashW[ord(s2[j]) - ord('a')] += 1

        return False
