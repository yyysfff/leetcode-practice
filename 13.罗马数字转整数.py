class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        for i in range(len(s)):
            if s[i]=='I':
                num+=1
                if i+1<len(s) and (s[i+1]=='V' or s[i+1]=='X'):
                    num-=2
            elif s[i]=='V':
                num+=5
            elif s[i]=='X':
                num+=10
                if i+1<len(s) and (s[i+1]=='L' or s[i+1]=='C'):
                    num-=20
            elif s[i]=='L':
                num+=50
            elif s[i]=='C':
                num+=100
                if i+1<len(s) and (s[i+1]=='D' or s[i+1]=='M'):
                    num-=200
            elif s[i]=='D':
                num+=500
            elif s[i]=='M':
                num+=1000
        return num
s=input()
p=Solution()
print(p.romanToInt(s))