class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:

    # NodeMgmt(0) => Node(0) 이 실행되며 data 0을 가지는 노드가 생성된다.
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def get_node(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)

    def insert_node(self, data, insert_node):
        node = self.head
        flag = True
        while flag:
            if node.data == data:
                flag = False
            else:
                node = node.next
        temp = node.next
        node.next = insert_node
        insert_node.next = temp


linkedlist1 = NodeMgmt(0)

for data in range(1, 10):
    linkedlist1.add(data)

linkedlist1.insert_node(1, Node(1.5))
linkedlist1.get_node()
