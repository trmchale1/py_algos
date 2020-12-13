### Singly Linked List
## Queue
# Notice the class and _init_ structure

class _Node:
    __slots__ = '_element', '_next'

    # Constructor 
    def __init__(self):
        self._head = None
        self.tail = None
        self._next = next

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    # write code for dequeue and enqueue
    def dequeue(self):
        if self.is_empty():
            raiseEmpty('Queue is empty')
        answer = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
