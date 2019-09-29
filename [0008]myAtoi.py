class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if(len(s) == 0):
            return 0
        rs = 0
        flag = 1
        if(s[0] == '+'):
            pass
            s = s[1:]
        elif(s[0] == '-'):
            flag = -1
            s = s[1:]
        for i in range(len(s)):
            if(s[i] >= '0' and s[i] <= '9'):
                rs *= 10
                rs += int(s[i])
            else:
                break
        rs *= flag
        if(rs < -2**31):
            rs = -2**31
        if(rs > 2**31-1):
            rs = 2**31-1
        return rs
        
            
