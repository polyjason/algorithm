class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.data = {}
        self.count = 0
        self.queue = []
        self.capacity = capacity
    # @return an integer
    def get(self, key):
        try:
            self.queue.remove(key)
            self.queue.insert(0,key)
        except ValueError:
            pass
        return self.data.get(key,-1)


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if not key in self.data and self.count == self.capacity:
            del self.data[self.queue.pop()]
            self.count -= 1
        if key not in self.data:
            self.count  +=1
        self.data[key] = value
        try:
            self.queue.remove(key)
        except ValueError:
            pass
        self.queue.insert(0,key)
        print 'after---',self.queue
lru = LRUCache(2)
lru.set(2,1)
lru.set(1,1)
print lru.get(2)
lru.set(4,1)
print lru.get(1)
print lru.get(2)
