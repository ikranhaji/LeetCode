class Solution(object):
    def removeElement(self, nums, val):
        right = 0
        while right < len(nums):
            if nums[right] == val:
                del nums[right]
            else:
                right += 1
        return len(nums)

            
            
        