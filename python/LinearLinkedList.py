from typing import Any

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        self.__curr = 0

    def __len__(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def addLast(self, val) -> None:
        newLast = Node(val)
        if self.isEmpty():
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = newLast
            self.tail = newLast

        self.size += 1

    def addFirst(self, val) -> None:
        newFirst = Node(val)

        if self.isEmpty():
            self.head = newFirst
            self.tail = newFirst
        else:
            newFirst.next = self.head
            self.head = newFirst

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
            current.next = newNode

            self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Can't remove an element from an empty list")

        rVal = self.head.val
        self.head = self.head.next

        self.size -= 1

        if self.isEmpty():
            self.tail = None

        return rVal

    def removeLast(self):
        if self.isEmpty():
            raise Exception("Can't remove an element from an empty list")

        current = self.head

        if current.next == None:
            rVal = current.val
            self.head = None

        else:
            while current.next.next != None:
                current = current.next

            rVal = current.val
            current.next = None
            self.tail = current

        self.size -= 1

        return rVal

    def removeAnywhere(self, index):
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
            current.next = current.next.next

        self.size -= 1
        return rVal

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if not (0 <= index < self.size):
            raise Exception("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val

    def __iter__(self):
        self.__curr = 0
        return self

    def __next__(self) -> Any:
        if self.__curr == self.size:
            raise StopIteration()

        rVal = self.get(self.__curr)
        self.__curr += 1

        return rVal

    def __str__(self) -> str:
        if self.size == 0:
            return "Empty List"

        display = ""

        current = self.head
        for _ in range(self.size):
            display += f"{current.val}" + (" -> "
                                           if current.next != None else "")
            current = current.next

        return display


if __name__ == "__main__":
    newList = LinkedList()

    newList.addFirst("first")

    print(newList)

    newList.addLast("last")

    print(newList)

    newList.addAnywhere("fourth", 1)
    newList.addAnywhere("third", 1)
    newList.addAnywhere("second", 0)

    print(newList)
