class Solution(object):
    def containsDuplicate(self, nums):
        numbers= set()
        for num in nums:
            if num in numbers:
                return True
            numbers.add(num)
        return False
            