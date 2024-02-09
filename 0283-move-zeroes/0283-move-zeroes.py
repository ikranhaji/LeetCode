class Solution(object):
    def moveZeroes(self, nums):
        right = 0
        left = len(nums)
        while right < left:
            if nums[right] == 0:
                nums.append(nums.pop(right))
                left -= 1
            else:
                right += 1
        return nums
