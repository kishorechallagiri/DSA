class Solution(object):
    def sortPeople(self, names, heights):
        people = list(zip(heights, names))
        people.sort(reverse=True)  # sort by height descending
        return [name for height, name in people]
        
        