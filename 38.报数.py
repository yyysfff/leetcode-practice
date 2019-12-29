class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        else:
            S=Solution()
            c_list=S.countAndSay(n-1)
            ans=""
            i=0
            for j in range(len(c_list)):
                if c_list[i]!=c_list[j]:
                    ans+=str(j-i)
                    ans+=str(c_list[i])
                    i=j
                if j==len(c_list)-1:
                    ans+=str(j-i+1)
                    ans+=str(c_list[i])
            return ans
num=int(input())
S=Solution()
print(S.countAndSay(num))