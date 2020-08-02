class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        s = word
        if s.upper() == word or s.lower() == word or s.capitalize()==word:
            return True
        return False