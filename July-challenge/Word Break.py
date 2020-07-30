class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hm={}
        return self.helper(s,wordDict,hm)
    def helper(self,s,wordDict,hm):
        if len(s) == 0:
            return True
        elif s in hm:
            return hm[s]
        for word in wordDict: # loop by word
            if s[0:len(word)] == word and self.helper(s[len(word):],wordDict,hm):
                hm[s] = True
                return True
        hm[s] = False
        return False

    # dp algo
    '''word = set(wordDict)
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True
    for i in range(len(s)):
        if not dp[i]: 
            continue
        # slower one: go through every position
        #for j in range(i + 1,len(s) + 1):
        #    if s[i:j] in word:
        #        dp[j] = True
        # go through the position at the length of possible word
        for w in word:
            if s[i:i+len(w)] == w:
                dp[i+len(w)] = True
    return dp[-1]'''