class Solution(object):
    def isPalindrome(self, x):
        new_x = str(x)
        return new_x == new_x[::-1]
            
        