class Solution(object):
    def twoSum(self, numbers, target):
        nums= {}
        for i, number in enumerate(numbers):
            difference = target - number
            if difference in nums:
                return [(nums[difference] + 1), (i + 1)]
            nums[number] = i
    
        