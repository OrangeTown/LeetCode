class Solution:
    def reverse(self, x: int) -> int:
        rs = 0
        flag = False
        if(x < 0):
            flag = True
            x = -x
        while(x != 0):
            rs *= 10
            rs += x % 10
            x = int(x / 10)
        if(flag):
            rs = -rs
        if(rs<-2**31 or rs>2**31-1):
            return 0
        return rs
