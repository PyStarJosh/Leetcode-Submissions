# Intuition
- This problem requires you to design a time-based key-value data structure that can store multiple values, so we know the data structure to initialize in our ```__init__``` constructor is a HashMap with separate chaining collision resolution.
  Since, we won't reassign the values at value or timestamp, a tuple is the better data structure to enforce immutability logic. So, our final data structure is a HashMap with a string key and list of tuples with two elements as the value.
- For ```set()```, we check if the key exist within the HashMap, if so, we simply append a tuple with the passed value and timestamp to the list. If not, we make a fresh list and append one tuple containing the passed value and timestamp arguments.
- For ```get()```, we check if the key exist within the HashMap, or if the timestamp argument is smaller than the smallest previous timestamp, if so, return "" as no value associates with the key or timestamp. To find the matching timestamp in the passed key arguments,
  we could use linear search, but our timestamps are in ascending order, so we can employ a binary search algorithm to reduce the number of operations to find our timestamp value. If the timestamp is not in the key's list, we must return the value with
  the closest previous_timestamp that is less than the passed timestamp.
- Finding the fallback case is based on a binary search pointer characteristic. In binary search when I value does not exist within the list, our ```left``` pointer points to the next larger value compared to the target and the ```right``` pointer points to the next smaller value compared to the target
- which is the value we need as the problem states the fallback timestamp is the largest previous timestamp less than the passed timestamp.

# Approach
1. Initialize our closed addressing HashMap
```python3 []
def __init__(self):
  self.pairs: dict[str, list[tuple[str, int]]] = {}
```
2. For ```set()```, check if the key is in the HashMap and append to existing or new array accordingly
```python3 []
def set(self, key: str, value: str, timestamp: int) -> None:
  self.pairs.setdefault(key, []).append((value, timestamp))
```
3. For  ```get()```, check if the key is in the HashMap and if the passed timestamp is smaller than all previous timestamps
```python3 []
def get(self, key: str, timestamp: int) -> str:
  if key not in self.pairs or timestamp < self.pairs[key][0][1]:
    return "
```
4. If both base conditions failed, perform binary search to find the passed timestamp in the HashMap if it exist, if not, return the timestamp in the tuple the right pointer is referencing
```python3 []
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
```

# Complexity
- Time complexity:
set(): O(1) -> Appending into a list is constant time unless underlying array needs to be resized
get(): O(log N) -> Binary search performed to find target timestamp
- Space complexity:
O(N) -> N represents number of key-value pairs in ```self.pairs ```

# Code
```python3 []
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
```
