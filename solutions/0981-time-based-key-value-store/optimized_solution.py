class TimeMap:

    def __init__(self):
        self.pairs: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pairs or timestamp < self.pairs[key][0][1]:
            return ""

        entries: list[tuple[str, int]] = self.pairs[key]
        left: int = 0
        right: int = len(self.pairs[key]) - 1

        while left <= right:
            mid: int = left + (right - left) // 2
            mid_timestamp: int = entries[mid][1]

            if mid_timestamp == timestamp:
                return entries[mid][0]
            elif mid_timestamp < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return entries[right][0]
