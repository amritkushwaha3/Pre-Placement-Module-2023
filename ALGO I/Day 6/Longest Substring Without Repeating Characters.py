class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest_str = ""
        for i, c in enumerate(s):
            canditate_str = str(c)
            for j in range(i + 1, len(s)):
                if s[j] not in canditate_str:
                    canditate_str += str(s[j])
                else:
                    break
            if len(canditate_str) > len(longest_str):
                longest_str = canditate_str
            if len(s) - i <= len(longest_str):
                break   
        return len(longest_str)