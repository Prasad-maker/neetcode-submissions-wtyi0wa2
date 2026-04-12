class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev=self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next


    def insert(self,node):
        node.next, node.prev = self.right,self.right.prev
        node.prev.next,self.right.prev = node,node


        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.capacity:
            k = self.left.next.key
            if k in self.cache:
                self.remove(self.left.next)
                del self.cache[k]
            

        
