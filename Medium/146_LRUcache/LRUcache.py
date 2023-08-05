class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.val}, {self.next}'

class LRUCache:

    # initialize a capacity value, a dictionary for the cache, and a head/tail for the start/end of the linked list queue
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def __repr__(self):
        return f'{self.head}'

    def get(self, key: int) -> int:
        # if the item is found, move it to the head of the linked list and then return the value stored in the node
        if key in self.cache:
            item = self.cache[key]
            item.val = value
            prev, next = item.prev, item.next
            if prev:
                prev.next = next
                next.prev = prev
            item.prev, item.next = None, self.head
            self.head = self.head.prev
            return item.val
        return -1


    def put(self, key: int, value: int) -> None:
        # if the key is in the cache, update the value and move it to the front of the list queue
        if key in self.cache:
            item = self.cache[key]
            item.val = value
            prev, next = item.prev, item.next
            if prev:
                prev.next = next
                next.prev = prev
            item.prev, item.next = None, self.head
            self.head = self.head.prev

        # otherwise we're creating a new node under several condition
        else:
            # if the cache is empty, create a new head node with value and default prev/next
            if len(self.cache) == 0:
                new_node = Node(value)
                self.head = new_node
                self.tail = self.head
                self.cache[key] = new_node

            # if the cache isn't empty, but also is not at capcity, add a new node to the end of the list and reassign
            # the tail pointer
            elif len(self.cache) < self.cap:
                new_node = Node(value)
                self.cache[key] = new_node
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = self.tail.next

            # if the cache is full, delete the key from the cache associated with the head node, advance the head node,
            # and clear the head prev reference. Then add a new node to the tail and reassign references
            else:
                del self.cache[self.head.val]
                self.head = self.head.next
                self.head.prev = None
                new_node = Node(value)
                self.cache[key] = new_node
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = self.tail.next



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