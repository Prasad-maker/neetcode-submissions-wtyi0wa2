class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for b in s:
            if b in "{[(":
                stack.append(b)
            else: 
                if stack:
                    com = stack.pop()
                    if b==")" and com!="(":
                        return False
                    elif b=="]" and com!="[":
                        return False
                    elif b=="}" and com!="{":
                        return False
                else:
                    return False
        if not stack:
            return True
        return False


        