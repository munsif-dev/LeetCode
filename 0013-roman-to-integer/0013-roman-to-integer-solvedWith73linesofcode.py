class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        value = 0
        while( i < n ):
            if i == n-1:
                match s[i] :
                    case "I" :
                        value += 1
                    case "V" :
                        value += 5
                    case "X" :
                        value += 10
                    case "L" :
                        value += 50
                    case "C" :
                        value += 100
                    case "D" :
                        value += 500
                    case "M" :
                        value += 1000
                return value
                
            match s[i]:
                case "I":
                    if s[i+1] == "V":
                        value += 4
                        i += 2
                    elif s[i+1] == "X":
                        value += 9
                        i += 2
                    else: 
                        value += 1
                        i += 1
                case "V":
                    value += 5
                    i += 1
                case "X":
                    if s[i+1] == "L":
                        value += 40
                        i += 2
                    elif s[i+1] == "C":
                        value += 90
                        i += 2
                    else: 
                        value += 10
                        i += 1
                case "L":
                    value += 50
                    i += 1
                case "C":
                    if s[i+1] == "D":
                        value += 400
                        i += 2
                    elif s[i+1] == "M":
                        value += 900
                        i += 2
                    else: 
                        value += 100
                        i += 1
                case "D":
                    value += 500
                    i += 1
                case "M":
                    value += 1000
                    i += 1
            
        return value
              