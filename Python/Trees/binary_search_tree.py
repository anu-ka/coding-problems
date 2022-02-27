class node:
    def __init__(self, val: int) -> None:
        self.left = None
        self.right = None
        self.val = val


class binarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: int) -> None:
        n = node(val)
        if self.root == None:
            self.root = n
        else:
            head = self.root
            while head != None:
                if val < head.val:
                    if head.left != None:
                        head = head.left
                    else:
                        head.left = n
                        return
                elif val > head.val:
                    if head.right != None:
                        head = head.right
                    else:
                        head.right = n
                        return

    def lookup(self, val: int) -> bool:
        head = self.root
        while head != None:
            if head.val == val:
                return True
            if val < head.val:
                print("Going left")
                head = head.left
            elif val > head.val:
                print("Going right")
                head = head.right
        return False


tree = binarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.lookup(9))
print(tree.lookup(4))
print(tree.lookup(6))
print(tree.lookup(20))
print(tree.lookup(170))
print(tree.lookup(15))
print(tree.lookup(1))
print(tree.lookup(60))
