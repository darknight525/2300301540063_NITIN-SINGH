class Solution(object):
    def uniqueOccurrences(self, arr):
        return len(set(Counter(arr).values()))==len(Counter(arr))
        