class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def addLast(self, val):
        newLast = Node(val)
        if self.isEmpty():
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = newLast

        self.tail = newLast

        self.size += 1

    def addFirst(self, val):
        newFirst = Node(val)

        if self.isEmpty():
            self.head = newFirst
            self.tail = newFirst
        else:
            newFirst.next = self.head
            self.head = newFirst

        self.size += 1

    def addAnywhere(self, val, index):
        if not (0 < index < self.size):
            return -1

        if self.isEmpty():
            self.addFirst(val)
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
            return -1

        rVal = self.head.val
        self.head = self.head.next

        self.size -= 1

        if self.isEmpty():
            self.tail = None

        return rVal

    def removeLast(self):
        if self.isEmpty():
            return -1

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
        if not (0 < index < self.size) or self.isEmpty():
            return -1

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

    def __str__(self) -> str:
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
    newList.addAnywhere("second", 1)

    print(newList)

    newList.removeAnywhere(2)

    print(newList)
