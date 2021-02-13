# 원형 데크

# MyCircularDeque(k) : 데크 사이즈 : k로 지정하는 생성자
# insertFront() : 데크 처음에 아이템을 추가하고 성공할 경우 True 리턴
# insertLast() : 데크 마지막에 아이템을 추가하고 성공할 경우 true 리턴
# deleteFront() : 데크 처음에 아이템을 삭제하고 성공할 경우 true
# deleteLast() : 데크 마지막에 아이템을 삭제하고 성공할 경우 true
# getFront() : 첫 아이템 가져옴 , 비어있다면 -1
# getRear() : 마지막 아이템 가져옴, 비어있다면 -1
# isEmpty() : 데크가 비어있는지 여부
# isFull() : 데크가 가득 차 있는지 여부


class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    # 두 노드 사이에 new 노드를 끼워넣음
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    # 노드 삭제
    # 다다음 노드를 연결시켜서 떼어냄
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False

        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
    
    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len els -1
    
    def isEmpty(self) -> bool:
        return self.len == 0
    
    def isFull(self) -> bool:
        return self.len == self.k