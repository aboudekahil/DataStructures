from typing import Any
from LinearLinkedList import LinkedList

class QueueLL:
    def __init__(self) -> None:
        self.data = LinkedList()

    def __len__(self) -> int:
        return len(self.data)

    def push(self, val) -> None:
        self.data.addFirst(val)

    def pop(self, index: int = 0) -> Any:
        return self.data.removeAnywhere(index)

    def insert(self, index: int, val) -> None:
        self.data.addAnywhere(val, index)

    def __str__(self) -> str:
        display = "[ "

        for i in self.data:
            display += f"{i} "

        return display + "]"

if __name__ == '__main__':
    qll = QueueLL()

    qll.push(4)
    qll.push(3)
    qll.push(2)
    qll.push(1)

    print(qll)
