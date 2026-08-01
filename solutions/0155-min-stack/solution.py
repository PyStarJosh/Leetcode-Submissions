class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.mins:
            self.mins.append(value)
        else: 
            if value <= self.mins[-1]:
                self.mins.append(value)

    def pop(self) -> None:
        popped_val = self.stack.pop()

        if popped_val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
