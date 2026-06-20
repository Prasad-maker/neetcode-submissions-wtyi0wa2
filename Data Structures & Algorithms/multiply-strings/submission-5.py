class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits=[0]*(len(num1)+len(num2))
        num1,num2 = num1[::-1],num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                total= int(num1[i1]) * int(num2[i2])+digits[i1+i2]
                digits[i1+i2]=total%10
                digits[i1+i2+1]+=total//10
                
        # carry = 0
        # for i in range(len(digits)):
        #     total = digits[i]+carry
        #     digits[i] = str(total%10)
        #     carry = total//10
        digits=digits[::-1]
        res = []
        mid =False
        for digit in digits:
            if digit!=0 or mid:
                res.append(str(digit))
                mid=True

        
        return "".join(res) if res else "0"

        