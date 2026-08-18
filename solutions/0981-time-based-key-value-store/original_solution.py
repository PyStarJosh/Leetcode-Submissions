class TimeMap:

    def __init__(self):
        self.pairs: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.pairs:
            self.pairs[key].append((value, timestamp))
            return
        self.pairs[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pairs or timestamp < self.pairs[key][0][1]:
            return ""

        left = 0
        right = len(self.pairs[key]) - 1

        while left <= right:
            mid: int = left + (right - left) // 2
            mid_timestamp: int = self.pairs[key][mid][1]
            mid_val: str = self.pairs[key][mid][0]

            if mid_timestamp == timestamp:
                return mid_val
            elif mid_timestamp < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return self.pairs[key][left - 1][0]
