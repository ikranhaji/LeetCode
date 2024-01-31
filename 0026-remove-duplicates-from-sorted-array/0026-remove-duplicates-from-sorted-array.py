class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                    del nums[i]
        return len(nums)