class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {"}":"{","]":"[",")":"("}
        for c in s:
            if c in "{[(":
                stack.append(c)
            else:

                if not stack or hmap[c]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False

        