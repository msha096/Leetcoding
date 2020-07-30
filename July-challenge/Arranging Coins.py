class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''num = 0
        acc = 0
        for i in range(1,n+1):
            acc+=i
            if acc>n:
                return num
            num+=1
        return num'''
        # math problem 
        k = int((2 * n) ** 0.5)
        s = k * (k + 1) // 2
        if s > n:
            #print ('o')
            return k-1
        return k