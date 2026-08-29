class Solution(object):
    def commonChars(self, words):
        hash = {}

        # Count characters in first word
        for ch in words[0]:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1

        # Check every other word
        for i in range(1, len(words)):

            current = {}

            # Count characters in current word
            for ch in words[i]:
                if ch not in current:
                    current[ch] = 1
                else:
                    current[ch] += 1

            # Update common frequencies
            for ch in list(hash.keys()):
                if ch in current:
                    hash[ch] = min(hash[ch], current[ch])
                else:
                    hash[ch] = 0

        # Create result
        lst = []

        for ch in hash:
            for i in range(hash[ch]):
                lst.append(ch)

        return lst
       
        
       