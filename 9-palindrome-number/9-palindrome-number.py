class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        ## using % to reverse the number
        temp_x = x
        reversed_num = 0
        while temp_x:
            reversed_num = reversed_num*10 + temp_x%10
            temp_x = temp_x//10
        
        print(x)
        print(reversed_num)
        
        if x==reversed_num:
            return True
        else:
            return False
            
        
        