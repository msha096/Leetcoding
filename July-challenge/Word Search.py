class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # backtracking, dp
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    copy = board[::1]
                    if self.helper(i,j,copy,word,0):
                        return True
        return False
    
    def helper(self,i,j,board,word,index):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i>= len(board) or j >= len(board[0]):
            return False
        if board[i][j] != word[index]:
            return False
        board[i][j] = 0
        if self.helper(i + 1, j, board, word, index + 1) or self.helper(i, j + 1, board, word, index + 1) or self.helper(i - 1, j, board, word, index + 1) or self.helper(i, j - 1, board, word, index + 1):
            return True
        board[i][j] = word[index] # key step of backtracking, to reverse the usage of current char
        return False