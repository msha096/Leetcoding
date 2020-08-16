class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # this can be extended to k transactions
        if prices == []:
            return 0
        day = len(prices)
        k = 2
        local = [[0 for j in range(k+1)] for i in range(day)] #
        globa = [[0 for j in range(k+1)] for i in range(day)]
        
        for i in range(1,day):
            diff = prices[i]-prices[i-1] 
            for j in range(1,k+1): # j: can make j transactions
                local[i][j] = max(globa[i-1][j-1], local[i-1][j]) + diff #local: made the last transaction on the i-th day
                globa[i][j] = max(globa[i-1][j], local[i][j])
        #print local
        #print globa
        return max(globa[-1]) #global[-1][2]

# ref: https://www.cnblogs.com/grandyang/p/4281975.html