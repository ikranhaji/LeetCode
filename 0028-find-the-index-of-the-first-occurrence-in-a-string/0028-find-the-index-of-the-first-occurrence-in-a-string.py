class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)