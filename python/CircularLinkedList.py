from typing import Any

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        
        self.__curr = self.head

    def __len__(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def addLast(self, val) -> None:
        newLast = Node(val)

        if self.isEmpty():
            self.head = newLast
            self.tail = newLast
        else:
            newLast.next = self.head
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
            self.tail.next = newFirst
            self.head = newFirst

        self.size += 1

    def addAnywhere(self, val, index: int) -> None:
        if self.isEmpty() and index == 0:
            self.addFirst(val)
            return
        
        if self.isEmpty() and index != 0:
            raise Exception("List is empty")

        if not (-1 <= index < self.size) and index != 0:
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

    def removeFirst(self) -> Any:
        if self.isEmpty():
            raise Exception("List is empty")

        rVal = self.head.val

        self.tail.next = self.head.next
        self.head = self.head.next

        self.size -= 1

        return rVal

    def removeLast(self) -> Any:
        if self.isEmpty():
            raise Exception("List is empty")

        rVal = self.tail.val

        current = self.head
        for _ in range(self.size - 2):
            current = current.next

        current.next = current.next.next
        self.tail = current

        self.size -= 1

        return rVal

    def removeAnywhere(self, index: int) -> None:
        if self.isEmpty():
            raise Exception("List is empty")

        if not (0 <= index < self.size):
            raise Exception("Index out of range")

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
    
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self.__curr == self.tail:
            raise StopIteration()
        
        rVal = self.__curr.val
        self.__curr = self.__curr.next

        return rVal
        
    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty List"

        display = ""

        current = self.head
        for _ in range(self.size):
            display += f"{current.val}" + (" -> "
                                           if current.next != None else "")
            current = current.next

        return display + (f"{self.head.val}" if self.size > 1 else "")


if __name__ == '__main__':
    cList = CircularLinkedList()

    cList.addFirst("First")
    cList.addLast("Last")
    cList.addAnywhere("fourth", 1)
    cList.addAnywhere("third", 1)
    cList.addAnywhere("second", 1)

    cList.clear()

    print(cList)
