class Treenode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


def max_level(root: Treenode) -> list[list[int]]:
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [root.val]

    return find_nodes(root, [])


def find_nodes(root: Treenode, result: list[list[int]]) -> list[list[int]]:
    if root == None:
        result.append([])
        return result
    if root.left == None and root.right == None:
        result.append([root.val])
        return result

    parent_queue = [root]
    child_queue = []

    while len(parent_queue) > 0 or len(child_queue) > 0:
        if len(parent_queue) > 0:
            parent_list = []
            while len(parent_queue) > 0:
                temp = parent_queue.pop()
                parent_list.append(temp.val)
                if temp.left != None:
                    child_queue.append(temp.left)
                if temp.right != None:
                    child_queue.append(temp.right)
            result.append(parent_list)

        if len(child_queue) > 0:
            child_list = []
            while len(child_queue) > 0:
                temp = child_queue.pop()
                child_list.append(temp.val)
                if temp.left != None:
                    parent_queue.append(temp.left)
                if temp.right != None:
                    parent_queue.append(temp.right)
            result.append(child_list)

    return result


one = Treenode(1)
two = Treenode(2)
three = Treenode(3)
four = Treenode(4)
five = Treenode(5)

one.left = two
one.right = three
three.left = four
four.left = five

print(max_level(one))
