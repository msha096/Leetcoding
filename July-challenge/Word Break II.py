class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # DP algo, before generate the results, we first verify the string by helper()
        dp = [[False,[]] for i in range(len(s)+1)]
        dp[0][0] = True
        word = set(wordDict)
        
        def helper():
            for i in range(len(s)):
                if not dp[i][0]:
                    continue
                for w in word:
                    if s[i:i+len(w)] == w:
                        dp[i+len(w)][0] = True
            return dp[-1][0]
        
        if not helper():
            return []
            
        for i in range(len(s)):
            if not dp[i][0]:
                continue
            for w in word:
                if s[i:i+len(w)] == w:
                    dp[i+len(w)][0] = True
                    if dp[i][1] == []:
                        dp[i+len(w)][1].append(w)
                    else:
                        for every in dp[i][1]:
                            dp[i+len(w)][1].append(every+' '+ w)
        return dp[-1][1]