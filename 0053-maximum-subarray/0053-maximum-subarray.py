class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) <= 1:
            return nums[0]
        max_sum = nums[0]
        current_sum = nums[0]
        for right in range(1, len(nums)):
            current_sum = max(nums[right], current_sum + nums[right])
            max_sum = max(max_sum, current_sum)

        return max_sum