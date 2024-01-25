class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest_word = ""
        current_word = ""
        for char in s:
            if char not in current_word:
                current_word += char
                if len(current_word) > len(longest_word):
                    longest_word = current_word
            else:
                index = current_word.index(char)
                current_word = current_word[index + 1 :] + char
        return len(longest_word)
