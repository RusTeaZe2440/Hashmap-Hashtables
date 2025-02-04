class Hashtables:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
        self.n = 0
        
    def __len__(self):
        return self.n 
    
    def __contains__(self, key):
        index = self._hashfunction(key)
        bucket = self.buckets[index]
        
        for (k,v) in bucket:
            if k == key:
                return True
        return False
    
    def put(self, key, value):
        index = self._hashfunction(key)
        bucket = self.buckets[index]
        
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.n += 1
            
    def get(self, key):
        index = self._hashfunction(key)
        bucket = self.buckets[index]
        
        for (k,v) in bucket:
            if k == key:
                return k,v
        return "No Key found"
        
    def remove(self, key):
        index = self._hashfunction(key)
        bucket = self.buckets[index]
        
        for i ,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.n -= 1
                break
        else:
            return 'Key not found'
        
    def keys(self):
        keys = [k for bucket in self.buckets for k, _ in bucket]
        return keys

    def values(self):
        values = [v for bucket in self.buckets for _, v in bucket]
        return values 
    def items(self):
        return [(k,v) for bucket in self.buckets for (k, v) in bucket]
    
    def _hashfunction(self, key):
        return abs(hash(key)) % self.size
    
h = Hashtables(5)
h.put('Bhavesh', 15)
h.put('Sahil', 15)
h.put('Deva',20 )
print(h.buckets)
h.put('Ghansu', 88)
h.put('Rutik', 33)
h.put('Akshata', 100)
h.put('Shiv', 43)
h.put('prathamesh', 55)
h.put('riya', 33)
h.put('Mohit', 77)
h.put('Kshitija', 88)
h.put('Shraddha', 66)
h.put('Gaurangi', 97)
print(h.buckets)
print(len(h))

h.remove('Bhavesh')
print(h.buckets)
print(len(h))
print(h.keys())
print(h.values())