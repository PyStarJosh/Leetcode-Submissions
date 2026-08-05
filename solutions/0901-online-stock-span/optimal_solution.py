class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.monotonic_stack and price >= self.monotonic_stack[-1][0]:
            _, prev_span = self.monotonic_stack.pop()
            span += prev_span

        self.monotonic_stack.append([price, span])

        return span
