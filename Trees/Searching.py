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
    depth_first_search(zero)

    print('Breadth first search')
    breadth_first_search(zero)


def visit(node):
    node.visited = True
    print(node.val)


def depth_first_search(root):
    if root is None:
        return False
    visit(root)
    for node in root.adjacent:
        if node.visited is False:
            depth_first_search(node)


def breadth_first_search(root):
    queue = []
    root.marked = True
    queue.append(root)

    while queue:
        node = queue.pop(0)
        visit(node)
        for child in node.adjacent:
            if not child.marked:
                child.marked = True
                queue.append(child)


if __name__ == '__main__':
    main()
