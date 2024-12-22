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

        if self.head == None:
            self.head = node

        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next

        iterator.next = node
        self.size += 1




