class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x_flag = True
            x = -x
        elif x > 0:
            x_flag = False
        else:
            return 0
        x_str = str(x)
        x_str = x_str[::-1]
        for i in range(len(x_str)):
            if x_str[i] != 0:
                x_str = x_str[i:]
                break
        if x_flag:
            x = int('-' + x_str)
        else:
            x = int(x_str)
        if x >= -2 ** 31 and x <= 2 ** 31 - 1:
            return x
        else:
            return 0
x=int(input())
p=Solution()
print(p.reverse(x))
