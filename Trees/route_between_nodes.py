from Trees.TernaryNode import TernaryNode


def main():
    zero = TernaryNode(0, [])
    one = TernaryNode(1, [])
    two = TernaryNode(2, [])
    three = TernaryNode(3, [])
    four = TernaryNode(4, [])
    five = TernaryNode(5, [])

    zero.adjacent.append(one)
    zero.adjacent.append(four)
    zero.adjacent.append(five)

    one.adjacent.append(three)
    one.adjacent.append(four)

    two.adjacent.append(one)

    three.adjacent.append(two)
    three.adjacent.append(four)

    print('Depth first search')
    print(depth_first_search(zero, 5))

    print()

    print('Breadth first search')
    print(breadth_first_search(zero, 5))


def visit(node, val):
    node.visited = True
    print(node.val)
    if node.val == val:
        return True
    return False


def depth_first_search(root, val):
    if root is None:
        return False
    if visit(root, val):
        return True
    for node in root.adjacent:
        if node.visited is False:
            if depth_first_search(node, val):
                return True
    return False


def breadth_first_search(root, val):
    queue = []
    root.marked = True
    queue.append(root)

    while queue:
        node = queue.pop(0)
        if visit(node, val):
            return True
        for child in node.adjacent:
            if not child.marked:
                child.marked = True
                queue.append(child)
    return False


if __name__ == '__main__':
    main()
