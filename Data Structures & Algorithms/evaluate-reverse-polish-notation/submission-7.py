class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s not in ['-','+','/','*']:
                stack.append(int(s))
            else:
                print(stack)
                n1=stack.pop()
                n2=stack.pop()
                if s=="+":
                    stack.append(n1+n2)
                elif s=="-":
                    stack.append(n2-n1)
                elif s=="*":
                    stack.append(n1*n2)
                elif s=="/":
                    print(n1,n2)
                    stack.append(int(n2/n1))
        return stack[-1]




        