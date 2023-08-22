class Solution(object):
    def reverseWords(self, s):
        new_s = s.split()[::-1]
        string = []
        for char in new_s:
            string.append(char)
        return " ".join(string)