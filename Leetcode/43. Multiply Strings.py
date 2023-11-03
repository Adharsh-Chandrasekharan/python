class Solution(object):
    def multiply(self, num1, num2):
        op=""
        n1=n2=0
        for i in range(len(num1)):
            n1+=(int(num1[i])*(10**(len(num1)-i-1)))
        for i in range(len(num2)):
            n2+=(int(num2[i])*(10**(len(num2)-i-1)))
        op=op+str(n1*n2)
        return op
        
    