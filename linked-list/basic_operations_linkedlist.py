class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def insert_after(self, node_value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current is not None:
            if current.value == node_value:
                new_node.next = current.next
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next

    def delete_node(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.nexte
        print("None")
my_list = LinkedList()

my_list.add(10)
my_list.add(20)
my_list.add(30)

my_list.print_list()  # Output: 10 -> 20 -> 30 -> None

print(my_list.search(20))  # Output: True
print(my_list.search(40))  # Output: False

my_list.insert_after(20, 25)
my_list.print_list()  # Output: 10 -> 20 -> 25 -> 30 -> None

my_list.delete_node(20)
my_list.print_list()  # Output: 10 -> 25 -> 30 -> None
