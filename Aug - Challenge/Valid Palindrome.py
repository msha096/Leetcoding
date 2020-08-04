class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        tmp = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                tmp.append(s[i])
        return tmp==tmp[::-1]