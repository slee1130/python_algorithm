# 큐 -> 한쪽 끝으로 자료를 넣고, 반대쪽에서는 자료를 뺄 수 있는 선형구조 -> first in first out ->fifo

def enqueue(self, value):
    new_node = Node(value)
    if self.is_empty():
        self.head = new_node
        self.tail = new_node
        return
    self.tail.next = new_node
    self.tail = new_node


def dequeue(self):
    if self.is_empty():
        return "queue is empty"
    delete_head = self.head
    self.head = self.head.next
    return delete_head.data


def peek(self):
    if self.is_empty():
        return "queue is empty"
    return self.head.data


def is_empty(self):
    return self.list.head is None
