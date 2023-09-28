class Solution(object):
    def intersect(self, nums1, nums2):
        intersect =[]
        for nums in nums1:
            if nums in nums2:
                intersect.append(nums)
                nums2.remove(nums)
        return intersect
                
        