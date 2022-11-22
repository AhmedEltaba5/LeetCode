class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n+1) # store n squares for each elem
        dp[0] = 0 # base case

        # calc squares
        i,s,squares = 1,1,[]
        while (s<=n):
          squares.append(s)
          i += 1
          s = i**2

        for target in range(1,n+1):
            for square in squares:
                if target-square < 0:
                    break
                dp[target] = min(dp[target], 1+dp[target-square])

        return dp[n]
        