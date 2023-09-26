class Solution(object):
    def reverse(self, x):
        limit=2**31
        neg=0
        if x<0:
            neg=-1
            x=x*-1  
        str1=str(x)
        str1=str1[::-1]
        int1=int(str1)
        if int1<=-limit or int1>=limit:
            return 0
        if neg==-1:
            int1=int1*(-1)
        return int1