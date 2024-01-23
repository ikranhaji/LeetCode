class Solution(object):
    def isPalindrome(self, s):
        new_s= ""
        for i in s:
            if i.isalnum():
                new_s += i
        final_s= new_s.lower()
        return final_s == final_s[::-1]
            
        