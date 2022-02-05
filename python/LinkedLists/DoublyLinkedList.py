from typing import Any


class Node:
    def __init__(self, val, next=None, previous=None) -> None:
        self.val = val
        self.next = next
        self.previous = previous


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def addFirst(self, val) -> None:
        newNode = Node(val)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    def addLast(self, val) -> None:
        lastNode = Node(val)

        if self.isEmpty():
            self.head = lastNode
            self.tail = lastNode
        else:
            lastNode.previous = self.tail
            self.tail.next = lastNode
            self.tail = lastNode

        self.size += 1

    def addAnywhere(self, val, index: int) -> None:
        if self.isEmpty() and index == 0:
            self.addFirst(val)
            return

        if self.isEmpty() and index != 0:
            raise Exception("List is empty")

        if not (-1 <= index < self.size):
            raise Exception("Index out of range")

        if index == 0:
            self.addFirst(val)
        elif index == -1:
            self.addLast(val)
        else:
            current = self.head
            newNode = Node(val)

            for _ in range(index - 1):
                current = current.next

            newNode.next = current.next
            newNode.previous = current
            current.next.previous = newNode
            current.next = newNode

            self.size += 1

    def removeFirst(self) -> Any:
        if self.isEmpty():
            raise Exception("List is empty")

        rVal = self.head.val

        self.head = self.head.next
        self.head.previous = None

        self.size -= 1

        return rVal

    def removeLast(self) -> Any:
        if self.isEmpty():
            raise Exception("List is empty")

        rVal = self.tail.val

        self.tail = self.tail.previous
        self.tail.next = None

        self.size -= 1

        return rVal

    def removeAnywhere(self, index: int):
        if not (0 <= index < self.size) or self.isEmpty():
            raise Exception("Index out of range or list is empty")

        if index == 0:
            return self.removeFirst()
        elif index == (self.size - 1):
            return self.removeLast()
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            rVal = current.next.val

            current.next.next.previous = current
            current.next = current.next.next

        self.size -= 1

        return rVal

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self) -> str:
        if self.size == 0:
            return "Empty List"

        display = ""

        current = self.head
        for _ in range(self.size):
            display += f"{current.val}" + (" ⇄ "
                                           if current.next != None else "")
            current = current.next

        return display


if __name__ == '__main__':
    dll = DoublyLinkedList()

    dll.addFirst("first")
    dll.addLast("second")
    dll.addLast("Last")
    dll.addAnywhere("last2", -1)

    print(dll)