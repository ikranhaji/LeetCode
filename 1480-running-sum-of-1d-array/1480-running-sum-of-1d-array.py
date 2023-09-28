class Solution(object):
    def runningSum(self, nums):
        final_sum = []
        for right in range(len(nums)):
            final_sum.append(sum(nums[:right + 1]))
        return final_sum
            