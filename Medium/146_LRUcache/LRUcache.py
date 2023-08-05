class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key, self.val = key, val
        self.next = self.prev = None

    def __repr__(self):
        return f'{self.val}, {self.next}'

class LRUCache:

    # initialize a capacity value, a dictionary for the cache, and a head/tail for the start/end of the linked list queue
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # head is Least Recently Used (LRU), tail is Most Recently Used (MRU)
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def __repr__(self):
        return f'{self.head}'

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # insert node at right end of list
    def insert(self, node):
        prev, next = self.tail.prev, self.tail
        node.prev, node.next = prev, next
        prev.next, self.tail.prev = node, node

    def get(self, key: int) -> int:
        # if the item is found, move it to the head of the linked list and then return the value stored in the node
        if key in self.cache:
            item = self.cache[key]
            self.remove(item)
            self.insert(item)
            return item.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key is in the cache, update the value and move it to the front of the list queue
        if key in self.cache:
            item = self.cache[key]
            item.val = value
            self.remove(item)
            self.insert(item)

        # otherwise we're creating a new node with several conditions
        else:
            # if the cache is not full, create a new node and add to right end of queue
            if len(self.cache) < self.cap:
                new_node = Node(key, value)
                self.cache[key] = new_node
                self.insert(new_node)

            # if the cache is full, delete the key from the cache associated with the left end of list and remove the
            # left most item from list. Then insert the new item.
            else:
                node = self.head.next
                del self.cache[node.key]
                self.remove(node)
                new_node = Node(key, value)
                self.cache[key] = new_node
                self.insert(new_node)



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(10)  #creates 10 capacity cache
obj.put(1, 1)  # creates key: val pair of 5, 55
obj.put(2, 2)  # creates key: val pair of 5, 55
obj.put(3, 3)  # creates key: val pair of 5, 55
obj.put(4, 4)  # creates key: val pair of 5, 55
obj.put(5, 5)  # creates key: val pair of 5, 55
obj.put(6, 6)  # creates key: val pair of 5, 55
obj.put(7, 7)  # creates key: val pair of 5, 55
obj.put(8, 8)  # creates key: val pair of 5, 55
obj.put(9, 9)  # creates key: val pair of 5, 55
obj.put(10, 10)  # creates key: val pair of 5, 55
print(obj)
print(obj.cache)
obj.put(11, 11)  # creates key: val pair of 5, 55
print(obj)
print(obj.cache)

"""
obj.put(6, 6)  # creates key: val pair of 5, 55
obj.put(7, 7)  # creates key: val pair of 5, 55
obj.put(8, 8)  # creates key: val pair of 5, 55
obj.put(9, 9)  # creates key: val pair of 5, 55
obj.put(10, 10)  # creates key: val pair of 5, 55
print(obj.cache)
print(obj.queue)
obj.put(9, 99)  # creates key: val pair of 5, 55
obj.put(10, 100)  # creates key: val pair of 5, 55
print(obj.cache)
print(obj.queue)
obj.put(11, 11)  # creates key: val pair of 5, 55
print(obj.cache)
print(obj.queue)
obj.put(12, 12)  # creates key: val pair of 5, 55
print(obj.cache)
print(obj.queue)
obj.put(12, 144)  # creates key: val pair of 5, 55
print(obj.cache)
print(obj.queue)
print(obj.get(3))
print(obj.cache)
print(obj.queue)

obj.put(40, 44)  # creates key: val pair of 5, 55
print(obj.cache)
print(obj.queue)
"""


"""
My first solution acknowledging time complexity is greater than O(1).  It's O(n) for all get/put functions that reorder
the queue.  Linked lists are not used.

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = [-1] * capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            for i, num in enumerate(self.queue):
                if key == num:
                    self.queue.append(self.queue.pop(i))
            return self.cache[key]
        return -1
        # need to move this value to the front of the queue

    def put(self, key: int, value: int) -> None:
        # if the last value in the cache is -1 (i.e. the data capacity hasn't been reached yet, then merely create the
        # key, value pair, add the key to the front of the queue and pop the last value off the queue
        if key in self.cache:
            self.cache[key] = value
            for i, num in enumerate(self.queue):
                if key == num:
                    self.queue.append(self.queue.pop(i))
        else:
            if self.queue[0] == -1:
                self.cache[key] = value
                self.queue.pop(0)
                self.queue.append(key)

            # otherwise if there is a value other than -1 at the end of the queue (i.e. data capacity has been reached),
            # then take the first key in queue, remove it from the cache, pop it from the queue, and write the new value to
            # the cache
            else:
                LRU_item = self.queue.pop(0)
                del self.cache[LRU_item]
                self.cache[key] = value
                self.queue.append(key)
"""