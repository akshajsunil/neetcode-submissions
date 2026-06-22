class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.k = capacity
        

    def get(self, key: int) -> int:
        if key in self.d :
            self.d.move_to_end(key)
            return self.d[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.k:
            self.d.popitem(last=False)

        
