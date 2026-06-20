class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits=[0]*(len(num1)+len(num2))
        num1,num2 = num1[::-1],num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digits[i1+i2] += int(num1[i1]) * int(num2[i2])
        carry = 0
        for i in range(len(digits)):
            total = digits[i]+carry
            digits[i] = str(total%10)
            carry = total//10
        digits=digits[::-1]
        t=0
        for i in range(len(digits)-1):
            if digits[i]=="0":
                t=i+1
            else:
                break
        digits = digits[t:]
        return "".join(digits)

        