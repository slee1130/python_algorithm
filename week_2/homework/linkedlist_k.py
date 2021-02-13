# def get_kth_node_from_last(self, k):
#     length = 1  # 시작 노드의 길이를 세기 위해 1부터 시작합니다
#     cur = self.head
#
#     while cur.next is not None:
#         cur = cur.next
#         length += 1
#     end_length = length - k
#     cur = self.head
#     for i in range(end_length):
#         cur = cur.next
#     return cur

def get_kth_node_from_last(self, k):
    slow = self.head
    fast = self.head

    for i in range(k):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow


 # 반드시 루프를 한번만 돈다고 해서 시간복잡도가 더 나은것은 아님
#  두 솔루션 결국 링크드 리스트의 끝까지 가야 하므로 같은 o(n)의 성능을 가짐
# 두개의 공간값을 가ㅣㅈ고 이동해야하므로 비슷한 연산량 사용
# 따라서 두 번 도는것보다 한번도는게 무조건 빠르지는 않음