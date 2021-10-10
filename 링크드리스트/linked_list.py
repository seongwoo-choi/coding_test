class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 헤드 노드 생성
node1 = Node(1)

def add(data):
    # 헤드 노드로 초기화
    node = node1
    # 다음 노드가 있으면 node 를 다음 노드로 초기화
    while node.next:
        node = node.next
    # 추가하고자 하는 노드를 node.next 에 넣어준다.
    node.next = Node(data)

def search_node():
    # 헤드 노드 초기화
    node = node1
    # 다음 노드가 존재할 때 까지 반복
    while node.next:
        print(node.data)
        # 다음 노드로 이동
        node = node.next
    print(node.data)

# 2~9 데이터를 가지는 노드 생성
for num in range(2, 10):
    add(num)

# 노드 순회
search_node()