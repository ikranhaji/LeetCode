class Solution(object):
    def searchRange(self, nums, target):
        try:
            first = nums.index(target)
        except ValueError:
            return [-1,-1]
        second = 0
        for idx, num in enumerate(nums):
            if num == target and idx > second:
                second = idx
        return [first, second]
        