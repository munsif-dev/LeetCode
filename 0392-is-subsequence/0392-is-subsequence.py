class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j = 0
        i = 0
        n = 0
        while( i < len(t) and j < len(s)):
            if t[i] == s[j]:
                i += 1
                j += 1
                n += 1
            else: 
                i += 1
        
        if n == len(s):
            return True
        else:
            return False
        


