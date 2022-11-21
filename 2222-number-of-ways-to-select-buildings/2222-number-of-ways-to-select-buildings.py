class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        total = 0 # number of ways
        seen = [[0]*2 for _ in range(2)] # keep track of 0,1 and 10,01

        for i in range(N):
            current = int(s[i])

            total += seen[1][1 - current] # add count of 10 or 01
            seen[1][current] += seen[0][1 - current] # increment 10 or 01
            seen[0][current] += 1 # increment 0 or 1

        return total
        