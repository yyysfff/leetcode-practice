class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs=[]
        if len(s)%2==1 or len(s)==0:
            return False
        for i in s:
            if i=="(" or i=="{" or i=="[":
                strs.append(i)
            else:
                if len(strs)==0:
                    return False
                else:
                    j=strs.pop()
            if len(strs)>len(s)/2:
                return False
            if i=="]":
                if j!="[":
                    return False
            elif i==")":
                if j!="(":
                    return False
            elif i=="}":
                if j!="{":
                    return False
        if len(strs)==0:
            return True
        else:
            return False
s=input()
p=Solution()
print(p.isValid(s))