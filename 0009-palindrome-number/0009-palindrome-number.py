class Solution(object):
    def isPalindrome(self, x):
        new_x = str(x)
        if new_x == new_x[::-1]:
            return True
        return False