class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP approach, the dp[i] step can only be reached from dp[i-1] and dp[i-2]
        if n <= 2:
            return n
        dp = [ 0 for i in range(n+1)]
        '''dp[0] = 1
        for i in range(1,n + 1):
            for k in (1,2):
                dp[i] += dp[i-k] '''
        dp[1] = 1 # number of 
        dp[2] = 2 # number of different combiantions/ ways..
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        #print(dp)
        return dp[-1]
        # https://leetcode.com/articles/climbing-stairs/ 
        # other solution can be found here, recursive, Fibonacci...s
