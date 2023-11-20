class Solution(object):
    def jump(self, nums):
        n = len(nums)
    
        if n == 1:
            return 0

        jumps = 0
        max_reach = nums[0]
        steps_left = nums[0]

        for i in range(1, n - 1):
            steps_left -= 1

            if i + nums[i] > max_reach:
                max_reach = i + nums[i]

            if steps_left == 0:
                jumps += 1
                steps_left = max_reach - i

        return jumps + 1
