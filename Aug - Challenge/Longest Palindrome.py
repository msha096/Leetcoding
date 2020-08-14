class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        
        res = 0
        flag = False
        c = Counter(s)
        
        for key in c:
            if c[key] %2 == 0:
                res += c[key]
            else:
                flag = True
                res += c[key] -1
        if flag:
            res += 1 # the central one do not need to be symmetry
        return res