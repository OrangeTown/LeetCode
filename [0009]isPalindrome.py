class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):return False
        newx = 0
        temp = x
        while(temp != 0):
            newx *= 10
            newx += (temp % 10)
            temp //= 10
        if(newx == x):return True
        else:return False
