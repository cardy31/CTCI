from Trees.BinaryNode import BinaryNode


def main():
    root = BinaryNode(None, None, 20)

    root.left = BinaryNode(None, None, 2)

    root.right = BinaryNode(None, None, 6)

    root.right.left = BinaryNode(None, None, 5)
    root.right.right = BinaryNode(None, None, 7)

    root.left.left = BinaryNode(None, None, 1)
    root.left.right = BinaryNode(None, None, 3)

    print('In order')
    in_order_traversal(root)

    print('Pre order')
    pre_order_traversal(root)

    print('Post order')
    post_order_traversal(root)


def visit(node):
    print(node.val)


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)


def pre_order_traversal(node):
    if node is not None:
        visit(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        visit(node)


if __name__ == '__main__':
    main()
