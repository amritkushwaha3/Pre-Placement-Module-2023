class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        
        f = []
        
        for i in range(m + 1):
            f.append([])
            for j in range(n + 1):
                f[i].append(0)
                
        for i in range(m):
            for j in range(n):                
                if text1[i] == text2[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                    
                                    
        return f[m][n]