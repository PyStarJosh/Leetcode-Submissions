class MyHashMap:
    def __init__(self):
        self.size = 1024
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def _get_bucket(self, key) -> list[int]:
        return self.buckets[self._hash(key)]

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self._get_bucket(key)
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
