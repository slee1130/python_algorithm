# 스택-> 한쪽 끝으로만 자료를 넣고 뺄 수 있는 자료 구조 -> Last in first out -> lifo
# push(data): 맨 앞에 데이터 넣기
# pop(): 맨앞의 데이터 뽑기
# peek(): 맨 앞의 데이터 보기
# isEmpty(): 스택이 비었는지 안 비었는지 여부 반환해주기

def push(self, value):
    new_head: Node(value)
    new_head.next = self.head
    self.head = new_head

def pop(self):
    if self.is_empty():
        return "Stack is empty"
    delete_head = self.head
    self.head = self.head.next
    return delete_head

def peek(self):
    if self.is_empty():
        return "Stack is empty"
    return self.head.data

def is_empty(self):
    return self.head is None

