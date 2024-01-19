class Solution(object):
    def sumOfThree(self, num):
        if num % 3 != 0:
            return []

        middle_number = num // 3


        start = middle_number - 1


        return [start, start + 1, start + 2]