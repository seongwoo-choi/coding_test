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


# 어느 노드 뒤에 노드를 삽입할 것인지 설정
def insert_node(data, insert_node):
    # 헤드 노드 초기화해준다.
    node = node1
    # 플래그를 설정하여 값을 찾기 전까진 트루로 설정
    flag = True
    while flag:
        # 현재 노드의 데이터와 입력받은 데이터(어느 노드 뒤에 값을 삽입할 지 설정하는 노드) 와 같으면 flag False 로 설정
        if node.data == data:
            flag = False
        else:
            # 값이 같지 않으면 다음 노드로 이동
            node = node.next
    # temp 에 node.next 를 저장
    temp = node.next
    # 현재 노드의 next 값으로 중간에 삽입된 노드를 설정
    node.next = insert_node
    # 삽입된 노드의 next 값으로 temp 를 설정
    insert_node.next = temp


# 2~9 데이터를 가지는 노드 생성
for num in range(2, 10):
    add(num)

# 노드 순회
# search_node()

node3 = Node(1.5)
insert_node(1, node3)
search_node()
