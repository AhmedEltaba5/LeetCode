class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        map_nums = [['M',1000], ['CM',900], ['D',500], ['CD',400], ['C',100], ['XC', 90], ['L',50],
                   ['XL', 40], ['X',10], ['IX', 9], ['V',5], ['IV', 4], ['I', 1]]
        
        result = ""
        for k,v in map_nums:
            if num // v:
                count = num // v
                result += count * k
                num = num % v
                print(v)
                
        return result
            
        
        