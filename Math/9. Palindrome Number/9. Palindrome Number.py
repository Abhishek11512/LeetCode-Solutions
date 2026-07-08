class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        n=x
        if x<0:
            return False
        while n > 0:
            d = n%10
            r= (r*10)+d
            n=n//10
        return x==r


      