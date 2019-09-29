class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        head = s[::2*(numRows-1)]
        mid = ""
        for i in range(numRows - 2):
            j = i+1
            while(True):
                if(j >= len(s)):
                    break
                mid += s[j]
                j += 2*(numRows-1)-2*(i+1)
                if(j >= len(s)):
                    break
                mid += s[j]
                j += 2*(i+1)
        end = s[numRows-1::2*(numRows-1)]
        return head+mid+end
