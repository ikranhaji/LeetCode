class Solution(object):
    def isPalindrome(self, s):
        final_s =[]
        new_s = s.lower().split()
        for char in new_s:
                for letter in char:
                    if letter.isalnum():
                        final_s.append(letter)

        final = "".join(final_s).replace(',', "")
        return final == final[::-1]
        