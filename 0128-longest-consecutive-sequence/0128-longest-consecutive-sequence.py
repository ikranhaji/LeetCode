class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
    
        new_num = sorted(set(nums))
        result = [new_num[0]]
        max_length = 1

        for right in range(1, len(new_num)):
            if new_num[right] == new_num[right - 1] + 1:
                result.append(new_num[right])
            else:
                max_length = max(max_length, len(result))
                result = [new_num[right]]

        return max(max_length, len(result))


        