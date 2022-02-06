class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.count = 0
        self.height = -1

    def __len__(self) -> int:
        if self.height == -1:
            raise Exception("Empty tree")

        return self.height

    def createRoot(self, val) -> None:
        self.root = Node(val)
        self.count += 1
        self.height += 1

    def fillTree(self, node) -> None:
        if self.root == None:
            raise Exception("Empty tree")
