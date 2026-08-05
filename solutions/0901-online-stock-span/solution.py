class StockSpanner:

    def __init__(self):
        self.prices = [] 
        self.spans = []

    def next(self, price: int) -> int:
        count = 1
        if not self.prices or price < self.prices[-1]:
            self.prices.append(price)
            self.spans.append(count)

        else:
            while self.prices and price >= self.prices[-1]:
                popped_span = self.spans.pop()
                self.prices.pop()
                count += popped_span

            self.prices.append(price)
            self.spans.append(count)

        return self.spans[-1]
