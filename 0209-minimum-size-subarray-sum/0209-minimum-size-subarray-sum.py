class Solution(object):
    def minSubArrayLen(self, target, nums):
        length= float('inf')
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target and left <= right:
                length = min(length, right - left + 1)
                sum -= nums[left]
                left = left + 1
        if length == float('inf'):
            return 0
        return length 
                
                
        
        