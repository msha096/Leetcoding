class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        dp = [[0,0,0] for i in range(len(prices))]  # i,0 : hold, i,1: buy, i,2: sell
        dp[0][1] = -prices[0]
        
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][2], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i]
        #print(dp)
        return max(dp[-1][0],dp[-1][2])