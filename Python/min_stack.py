import math


class MinStack:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.minStack: list[int] = []

    def push(self, val: int):
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            x = min(val, self.getMin())
            self.minStack.append(x)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

temp = MinStack()
temp.push(1)
temp.push(2)
print(temp.top())
print(temp.getMin())
print(temp.pop())
print(temp.getMin())
print(temp.top())
