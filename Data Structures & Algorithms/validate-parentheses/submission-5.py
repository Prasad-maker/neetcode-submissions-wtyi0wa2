class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "[({":
                stack.append(c)
            elif not stack:
                return False
            elif c == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif c == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return True if not stack else False
                


        