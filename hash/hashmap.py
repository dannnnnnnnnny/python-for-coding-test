import collections 


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
    
    def put(self, key: int, value: int) -> None:
        index = key % self.size # 나머지를 해시값으로 (단순하게)

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 해시 충돌 발생시 (개별 체이닝 방식)
        p = self.table[index] # p : 인덱스의 첫번째 값
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key, value) # 새 노드 생성 후 연결
    
    def get(self, key: int) -> int:
        index = key % self.size
        
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        
        if self.table[index].value is None:
            return
        
        # 1. 인덱스의 첫 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next

        # 2. 연결 리스트 노드 삭제
        # prev : 이전 노드 ,  p : 현재 노드
        # p.next 로 탐색하다가 일치하는 노드 찾으면
        # 이전 노드의 다음을 현재 노드의 다음으로 연결
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

    
