class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        map_dict = dict()
        map_dict['I'] = 1
        map_dict['V'] = 5
        map_dict['X'] = 10
        map_dict['L'] = 50
        map_dict['C'] = 100
        map_dict['D'] = 500
        map_dict['M'] = 1000
        
        prev = 0
        res = 0
        for i in s:
            if prev < map_dict[i]:
                res = res + map_dict[i] - 2 * prev
            else:
                res = res + map_dict[i]
            prev = map_dict[i]
            
        return res
            
        