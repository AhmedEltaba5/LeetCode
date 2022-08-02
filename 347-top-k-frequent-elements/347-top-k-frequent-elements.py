class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # bucket sort O(n)
        
        # index is count and value is list of nums with this count
        freq_list = [[] for i in range(len(nums) + 1)] 
        
        count_dict = dict()
        for elm in nums:
            count_dict[elm] = count_dict.get(elm,0) + 1
        
        for num, count in count_dict.items():
            freq_list[count].append(num)
            
        top_k = []
        
        for i in freq_list[::-1]:
            if i:
                for elm in i:
                    top_k.append(elm)
                    if len(top_k) == k:
                        return top_k
            