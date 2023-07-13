"""
Implementation of MinStack using built in Python data-structure.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        self.stack.pop()
        for num in self.stack:
            self.minimum = min(self.minimum, num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum if type(self.minimum) == int else None

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_3 = obj.top()
print(param_3)
minimum = obj.getMin()
print(minimum)
obj.pop()
minimum = obj.getMin()
print(minimum)
"""

"""
The following is an approach that uses a doubly linked list as the basis for the MinStack, with a separate class for
nodes of the list. 
"""
class StackNode:
    def __init__(self, val):
        self.val = val
        self.minimum = float('inf')
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'(Val: {self.val}, Min: {self.minimum}), {self.next}'

class MinStack:

    def __init__(self):
        self.head = None
        self.top_node = None

    def __repr__(self):
        return f'{self.head}'

    def push(self, val: int) -> None:
        if not self.top_node:
            self.top_node = StackNode(val)
            self.head = self.top_node
            self.top_node.minimum = val
        else:
            new_node = StackNode(val)
            new_node.prev = self.top_node
            new_node.minimum = min(self.top_node.minimum, new_node.val)
            self.top_node.next = new_node
            self.top_node = self.top_node.next

    def pop(self) -> None:
        self.top_node = self.top_node.prev
        self.top_node.next = None

    def top(self) -> int:
        return self.top_node.val

    def getMin(self) -> int:
        return self.top_node.minimum


minstack = MinStack()
minstack.push(3)
minstack.push(5)
minstack.push(-1)
minstack.push(15)
print(minstack.head)
print(minstack.top_node)
minstack.pop()
print(minstack.head)
