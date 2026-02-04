class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        if self.first is None:
            self.first = Node(value, None)
            self.last = Node(value, None)
        else:
            new_last = Node(value, None)
            self.last.next = new_last 

pampalini = LinkedList()
pampalini.add(1)
pampalini.add(2)
pampalini.add(3)
             