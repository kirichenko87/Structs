class Node:

    def __init__(self, data: any, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def add(self, elem):
        node = Node(data=elem, next=None)

        if self.size == 0:
            self.add_head(node)
        else:
            iterator = self.head
            while iterator.next != None:
                iterator = iterator.next

            iterator.next = node
            self.size += 1

    def add_head(self, elem: any) -> None:
        node = Node(data=elem, next=self.head)

        self.head = node
        self.size += 1

    def is_empty(self) -> bool:
        return False if self.size == 0 else True





ll = LinkedList()

ll.add(11)
ll.add(12)
ll.add(13)
print(ll.size)



ll.add_head(11)
ll.add_head(123)
ll.add_head(1234)
ll.add_head("hi")
print(ll.size)
