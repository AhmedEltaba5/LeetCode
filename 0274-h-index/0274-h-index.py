class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n_papers = len(citations)
        citations.sort()
        for i in range(n_papers):
            h_index = n_papers-i
            if citations[i]>=h_index:
                return h_index
        return 0
        