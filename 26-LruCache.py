class LRUCache:
    def __init__(self, capacity: int):
        self.lru={}
        self.capacity=capacity
        self.last=None

    def get(self, key: int) -> int:
        return self.lru.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if len(self.lru)==self.capacity:
            self.lru.pop(self.last)
            self.lru.update({key:value})
            self.last=key
        else:
            self.lru.update({key:value})

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param_1 = obj.get("key")
obj.put("key",1)
obj.put("key",1)
obj.put("key",1)
obj.put("key",1)
obj.put("key",1)
obj.put("key",1)