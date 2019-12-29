class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while(digits[i]==9 and i!=0):
            digits[i]=0
            i-=1
        if i!=0:
            digits[i]+=1
            return digits
        else:
            if digits[0]!=9:
                digits[0]+=1
                return digits
            else:
                digits[0]=0
                digits.insert(0,1)
                return digits