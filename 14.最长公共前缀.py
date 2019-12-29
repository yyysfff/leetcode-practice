class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        num=len(strs[0])
        for str_s in strs:
            if num>len(str_s):
                num=len(str_s)
            if num==0:
                return ''
            for i in range(num):
                num=i
                if str_s[i]!=strs[0][i]:
                    num-=1
                    break
            num+=1
            if num==0:
                return ''
        return strs[0][:num]
strs=input().split(",")
s=Solution()
print(s.longestCommonPrefix(strs))