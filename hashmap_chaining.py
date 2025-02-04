
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n 
    
    def insert_tail(self, key, value):
        newnode = Node(key, value)
        if self.head == None:
            self.head = newnode
        else:

            curr = self.head
            while curr.next:
                curr = curr.next 
        
            curr.next = newnode
        self.n += 1

    def search(self,key):
        curr = self.head
        pos = 0
        while curr:
            if curr.key == key:
                return pos
            
            curr = curr.next
            pos += 1
        return 'Key not found'
        
    def remove(self,key):
        curr = self.head
        while curr:
            if curr.next.key == key:
                break
            curr = curr.next
        if curr is None:
            return 'item not found'
        else:
            curr.next = curr.next.next 

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.key,'->',curr.value,end=' ')
            curr = curr.next

LL = LinkedList()
class Hashmap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self._make_array(capacity)
    
    def _make_array(self,capacity):
        L = []
        for i in range(capacity):
            L.append(LL)
        return L
    
    def put(self,key,value):
        index = self.hashfunction(key)

        pass
    def get_linked_List(self,index,key):
        self.buckets[index].search()

    def hashfunction(self,key):
        return abs(hash(key)) % self.capacity
    
h = Hashmap(10)
print(h.buckets)