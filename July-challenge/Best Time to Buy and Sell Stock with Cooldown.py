class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        # difficulity: medium
        # dp algorithm, with O(n) running time
        # space can be saved by using three int buffers to store the value, instead of using n*3 list
        # state machine: rest can be transisted from sell, or stay at resting since yesterday
        # hold (have stock) can be transisted from rest + buy stock, or remain holding as yesterday
        # sell: can only be transisted from holding  
        if len(prices) < 2:
            return 0
        
        dp = [[0,0,0] for i in range(len(prices))]  # i,0 : rest, i,1: hold, i,2: sell
        dp[0][1] = -prices[0]
        
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][2], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i]
        #print(dp)
        return max(dp[-1][0],dp[-1][2])
