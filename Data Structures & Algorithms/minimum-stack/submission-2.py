class MinStack:


    def __init__(self):
        self.stack =[]
        self.stack_min=float("infinity")
        

    def push(self, val: int) -> None:
        self.stack.append([val,min(val,self.stack_min)])
        self.stack_min = min(val,self.stack_min)
        

    def pop(self) -> None:
        element = self.stack.pop()
        if self.stack:
            self.stack_min=self.stack[-1][1]
        else:
            self.stack_min=float("infinity")
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack_min
        
