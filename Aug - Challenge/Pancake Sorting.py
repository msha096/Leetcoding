class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # pancake algorithm
        # find the maximum number and put it to the back
        res = list()
        for i in range(len(A), 1, -1):
            idx = A.index(i)
            #print idx,A,A[:idx:-1]
            A = A[:idx:-1] + A[:idx]
            res += [idx + 1, i]
            
        return res