class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                  return mid
            if target > nums[mid]:
                  left = mid + 1
            else:
                right = mid - 1
        return left