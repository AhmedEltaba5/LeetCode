class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        res = []
        if len(nums1_set)<=len(nums2_set):
            # loop over nums1_set
            for i in nums1_set:
                if i in nums2_set:
                    for _ in range(min(nums1.count(i), nums2.count(i))):
                        res.append(i)
        else:
            # loop over nums2_set
            for i in nums2_set:
                if i in nums1_set:
                    for _ in range(min(nums1.count(i), nums2.count(i))):
                        res.append(i)
        return res