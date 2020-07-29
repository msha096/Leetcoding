class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ''' method 1
        s = str(num)
        while len(s)>1:
            n = 0
            for i in range(len(s)):
                n+=int(s[i])
            s = str(n)
        return int(s)'''
        # method 2: digital root are same : x and x+9
        if num < 10:
            return num
        return 1 + (num - 1) % 9