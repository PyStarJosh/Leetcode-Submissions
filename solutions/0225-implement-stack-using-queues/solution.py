class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

        for _ in range(len(self.q1) - 1):
            val = self.q1.pop(0)
            self.q1.append(val)
        
    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0
