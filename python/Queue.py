class Queue:
    def __init__(self) -> None:
        self.data = []

    def __len__(self) -> int:
        return len(self.data)

    def push(self, val) -> None:
        self.data.insert(0, val)
    
    def insert(self, index: int, val) -> None:
        self.data.insert(index, val)

    def pop(self, index: int = -1):
        return self.data.pop(index)

    def __str__(self) -> str:
        return f"{self.data}"

if __name__ == '__main__':
    nq = Queue()

    nq.push(1)
    nq.push(2)
    nq.push(3)
    nq.push(4)
    nq.pop(5)
    print(nq)
