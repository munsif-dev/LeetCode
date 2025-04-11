
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [s.join(a) for a in s if a.isalpha() or a.isdigit()]
        

        l = 0
        r = len(s) - 1

        while(l <= r):
            print(s[l], s[r])
            if(s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return False
        
        return True


        