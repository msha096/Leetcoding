class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        # can use enumerates and verify valid maximum time
        s1 = {0,1,2}
        s2 = {0,1,2,3}
        a = set(A)
        if not s1.intersection(a):
            return ''
        res = ''
        B = A [::]
        def helper(res):
            t1 = res[0]*10+res[1]
            t2 = res[1]*10+res[0]
            if 0<=t1<60 and 0<=t2<60:
                return str(max(t1,t2))
            elif 0<=t1<60:
                return str(t1)
            elif 0<=t2<60:
                return str(t2)
            return ''
        if 2 in A:
            A.remove(2)
            a = set(A)
            clock = s2.intersection(a)
            if not clock:
                return ''
            else:
                m = max(clock)
                A.remove(m)
                res = '2'+str(m)
                k = helper(A)
                if k:
                    if len(k)==1:
                        k = '0'+k
                    return res+':'+k
                else:
                    res = ''
                    A = B[::]
                    
        for k in (1,0):
            if k in A:
                A.remove(k)
                c = max(A)
                res = str(k)+str(c)
                A.remove(c)
                m = helper(A)
                if m:
                    if len(m) == 1:
                        m = '0' + m
                    return res+':'+m
                else:
                    res = ''
                    A = B[::]
        return ''
      
                    