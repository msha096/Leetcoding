class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1 :
            return [0,1,2,3,4,5,6,7,8,9]
        d = {i:[] for i in range(10)}
        for i in range(10):
            if K != 0:
                if i + K <= 9:
                    d[i].append(i + K)
                if i - K >= 0:
                    d[i].append(i - K)
            else:
                d[i].append(i) # avoid duplicate
                
        q = ['1','2','3','4','5','6','7','8','9']
        res = []
        
        while q:
            top = q.pop()
            if len(top) < N:
                for neigh in d[int(top[-1])]:
                    q.append(top+str(neigh))
            elif len(top) == N:
                res.append(int(top))
        return sorted(res)
        