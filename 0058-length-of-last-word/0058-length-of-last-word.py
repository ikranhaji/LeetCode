class Solution(object):
    def lengthOfLastWord(self, s):
        new_s = s.strip().split(' ')
        return len(new_s[-1])
        