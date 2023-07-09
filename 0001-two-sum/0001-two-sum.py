class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_dict:
                return [num_dict[difference] , i]
            num_dict[num] = i
        return []
                        
                        
                        
            
           