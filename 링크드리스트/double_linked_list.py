class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            newNode = Node(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode

    def get_node(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.next
        return False


    def search_from_tail(self, data):
        if self.tail == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.prev
        return False

    def insert_before_node(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return self.head.data
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new


double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)

double_linked_list.insert_node(1.5, 1)
double_linked_list.get_node()