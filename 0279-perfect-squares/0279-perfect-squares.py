class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i,k,squares = 1,1,[]
        while (k<=n):
          squares.append(k)
          i += 1
          k = i**2

        dp = [float('inf') for _ in range(n+1)]

        for s in squares:
          for i in range(1,n+1):
            if s <= i:
              if i % s == 0:
                can = i // s
                dp[i] = min(can, dp[i])
              else:
                dp[i] = min(1+dp[i-s], dp[i])
        return dp[n]
        