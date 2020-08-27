class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        '''
        #TLE
        day = set(days)
        last = [1,7,30]
        stop = days[-1]
        
        def dp(i,stop):
            if i > stop:
                return 0
            elif i in day:
                return min(dp(i+d,stop)+c for d,c in zip(last,costs))
            else:
                return dp(i+1,stop)
        return dp(1,stop)'''
        
        day = set(days)
        n = days[-1]+1
        dp =[0]*n
        for i in range(1,n):
            if i not in days:
                dp[i] = dp[i-1]
                continue
            dp[i] = min(dp[max(0,i-1)]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
        return dp[-1]