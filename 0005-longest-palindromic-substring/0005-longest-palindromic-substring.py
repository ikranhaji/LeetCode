class Solution(object):
    def longestPalindrome(self, s):
        longest= ""
        current = ""
        for i in range(len(s)):
            l=r=i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                current = s[l:r + 1]
                l -= 1
                r += 1
                if len(current) > len(longest):
                      longest = current
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                current = s[l:r + 1]
                l -= 1
                r += 1
                if len(current) > len(longest):
                      longest = current
        return longest