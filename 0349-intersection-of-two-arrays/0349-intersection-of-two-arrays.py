class Solution(object):
    def intersection(self, nums1, nums2):
        intersect=[]
        for num in nums1:
            if num in nums2:
                intersect.append(num)
                nums2.remove(num)
        return set(intersect)