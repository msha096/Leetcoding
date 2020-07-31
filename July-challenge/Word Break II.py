class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # DP algo, before generate the results, we first verify the string by helper()
        ''' # DP algo is 98% faster
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
        return dp[-1][1]'''

        # recursive and provide a more efficient validation method by comparing set
        # 86% faster
        word = set(wordDict)
        d = set(''.join(wordDict)) #concatenate into a string and split by using set
        st = set(s)
        
        if st - d: # if st contains some char that not exist in the word dict
            return [] # quick verify
        res = []
        n = len(s)
        def dfs(ans = [], ind = 0):
            if ind == n:
                res.append(' '.join(ans))
                return
            for i in range(ind,n+1):
                if s[ind:i] in word:
                    dfs(ans+[s[ind:i]],i)
        dfs()
        return res