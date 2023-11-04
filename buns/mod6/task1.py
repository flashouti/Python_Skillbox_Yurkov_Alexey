class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def get(self, index):
        if index < 0:
            return None
        current_node = self.head
        for i in range(index):
            if current_node is None:
                return None
            current_node = current_node.next
        if current_node is None:
            return None
        return current_node.value

    def remove(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        current_node = self.head
        prev_node = None
        for i in range(index):
            if current_node is None:
                return
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        if prev_node.next is None:
            self.tail = prev_node

    def insert(self, index, value):
        if index < 0:
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        current_node = self.head
        prev_node = None
        for i in range(index):
            if current_node is None:
                return
            prev_node = current_node
            current_node = current_node.next
        new_node.next = current_node
        prev_node.next = new_node
        if current_node is None:
            self.tail = new_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next