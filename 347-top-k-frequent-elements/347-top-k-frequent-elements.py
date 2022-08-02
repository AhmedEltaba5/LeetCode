class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count_dict = dict()
        for elm in nums:
            if elm in count_dict:
                count_dict[elm] += 1
            else:
                count_dict[elm] = 1
            
        return [i[0] for i in sorted(count_dict.items(), key=lambda x: x[1], reverse=True)][:k]