class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if not carry:
                return digits
            total = digits[i]+carry
            carry = 0
            digits[i]=total%10
            if total>=10:
                carry = total//10

        return digits if not carry else [carry]+digits
    
        