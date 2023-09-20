class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest_substring= ''
        current_substring= ''
        for char in s:
            if char not in current_substring:
                current_substring += char
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
            else:
                index = current_substring.index(char)
                current_substring = current_substring[index +1:] + char

        return len(longest_substring)