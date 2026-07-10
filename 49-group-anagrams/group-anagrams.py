class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr not in map:
                map[sortedStr] = [s]
            else:
                map[sortedStr].append(s)
        return list(map.values())
      
            


