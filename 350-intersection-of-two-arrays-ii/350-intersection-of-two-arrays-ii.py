class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = []
        k=len(nums1)
        for i in range(k):
            if(nums1[i] in nums2):
                a.append(nums1[i])
                ind = nums2.index(nums1[i])
                nums2[ind]= '_'

        return a