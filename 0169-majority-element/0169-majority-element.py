class Solution(object):
    def majorityElement(self, nums):
        amount = {}
        for num in nums:
            if num not in amount:
                amount[num] = 1
            amount[num] += 1
        maximum = 0
        majority = 0
        for key, value in amount.items():
            if value > maximum:
                maximum = value
                majority = key
        return majority
