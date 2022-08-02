class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        
        return False
                    
                    
    def helper(self, board, i, j, word):
        if len(word) == 0:
            return True
        
        if i < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or j < 0:
            return False

        if board[i][j] != word[0]:
            return False
         
        word = word[1:]
        char = board[i][j]
        board[i][j] = '#'

        result = self.helper(board, i + 1, j, word) or self.helper(board, i - 1, j, word) or self.helper(board, i, j + 1, word) or self.helper(board, i, j - 1, word)
        
        board[i][j] = char
                
        return result