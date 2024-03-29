class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hashmap = defaultdict(list)
        for s in strs:
            # keys can be strings, bcz they are immutable.
            hashmap[str(sorted(s))].append(s)
        return hashmap.values()
    
        """
        anagram_dict = {}
        
        for item in strs:
            item_sorted = ''.join(sorted(item))
            if item_sorted in anagram_dict.keys():
                anagram_dict[item_sorted].append(item)
            else:
                anagram_dict[item_sorted] = [item]
                
        return anagram_dict.values()
        """
                
                
        