class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.repository = {}
        self.rank = []

    def get(self, key: int) -> int:
        if key in self.repository:
            self.rank.remove(key)
            self.rank.append(key)
            return self.repository[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.repository:
            self.rank.remove(key)
        self.rank.append(key)
        self.repository[key] = value
        
        if len(self.repository) > self.capacity:
            self.repository.pop(self.rank.pop(0))

