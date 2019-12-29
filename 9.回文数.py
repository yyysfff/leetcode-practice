class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:
            return True
        if x<0 or x%10==0:
            return False
        else:
            temp_num=x
            temp=0
            while (x > 0):
                temp = temp * 10 + (x % 10)
                x //= 10
        if temp_num==temp:
            return True
        else:
            return False