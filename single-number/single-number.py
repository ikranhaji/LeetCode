class Solution(object):
    def singleNumber(self, nums):
        numbers = {}
        for num in nums:
                if num not in numbers:
                    numbers[num] = 1
                else:
                    numbers[num] += 1
        for key in numbers.keys():
            if numbers[key] <= 1:
                return key
        