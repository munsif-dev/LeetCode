class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split()
        n = len(s)
        s_n = [""] * n
        for i in range(n):
            print(i)
            s_n[-1-i] = s[i]
        
        return " ".join(s_n)

