from Trees.BinaryNode import BinaryNode


class BinaryTree:
    def __init__(self):
        self.head = None
        self.sorted_values = []

    def get_max(self):
        if self.head is None:
            return None

        node = self.head
        while node.right is not None:
            node = node.right
        return node.val

    def get_min(self):
        if self.head is None:
            return None

        node = self.head
        while node.left is not None:
            node = node.left
        return node.val

    def is_empty(self):
        return self.head is None

    def insert(self, val):
        # Empty tree
        if self.head is None:
            self.head = BinaryNode(None, None, val)
            return True

        node = self.head
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = BinaryNode(None, None, val)
                    return True
                else:
                    node = node.left
            elif val > node.val:
                if node.right is None:
                    node.right = BinaryNode(None, None, val)
                    return True
                else:
                    node = node.right
            else:
                return False

    def print_in_order(self):
        if not self.is_empty():
            self.__in_order_traversal(self.head)
        else:
            print('Tree is empty')

    def print_pre_order(self):
        if not self.is_empty():
            self.__pre_order_traversal(self.head)
        else:
            print('Tree is empty')

    def print_post_order(self):
        if not self.is_empty():
            self.__post_order_traversal(self.head)
        else:
            print('Tree is empty')

    def get_sorted(self):
        self.sorted_values = []
        self.__in_order_traversal_w_appends(self.head)
        return self.sorted_values

    def __in_order_traversal_w_appends(self, node):
        if node is not None:
            self.__in_order_traversal_w_appends(node.left)
            self.sorted_values.append(node.val)
            self.__in_order_traversal_w_appends(node.right)

    def __in_order_traversal(self, node):
        if node is not None:
            self.__in_order_traversal(node.left)
            print(node.val)
            self.__in_order_traversal(node.right)

    def __pre_order_traversal(self, node):
        if node is not None:
            print(node.val)
            self.__pre_order_traversal(node.left)
            self.__pre_order_traversal(node.right)

    def __post_order_traversal(self, node):
        if node is not None:
            self.__post_order_traversal(node.left)
            self.__post_order_traversal(node.right)
            print(node.val)

    def rebalance_tree(self):
        arr = self.get_sorted()
        self.head = None
        mid = int(len(arr) / 2)

        self.insert(arr[mid])
        for i in range(0, len(arr)):
            if i == mid:
                continue
            self.insert(arr[i])

    def get_depth(self):
        return self.__get_depth_internal(self.head)

    def __get_depth_internal(self, node):
        if node is None:
            return 0
        else:
            left_depth = self.__get_depth_internal(node.left)
            right_depth = self.__get_depth_internal(node.right)

            return max(left_depth, right_depth) + 1

    def list_per_depth(self):
        lists = []
        self.__list_per_depth(0, self.head, lists)
        return lists

    def __list_per_depth(self, depth, node, lists):
        if node is None:
            return lists
        if depth >= len(lists):
            lists.append(LinkedList())
        lists[depth].insert(node.val)

        self.__list_per_depth(depth + 1, node.left, lists)
        self.__list_per_depth(depth + 1, node.right, lists)

        return lists

    def balanced(self):
        if self.__balanced(0, self.head) == -1:
            return False
        return True

    def __balanced(self, depth, node):
        if node is None or depth == -1:
            return depth

        left_depth = self.__balanced(depth + 1, node.left)
        right_depth = self.__balanced(depth + 1, node.right)

        if left_depth == -1 or right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1

    def validate_bst(self):
        return self.__validate_bst(self.head, None, None)

    def __validate_bst(self, node, min_val, max_val):
        if node is None:
            return True

        if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val > max_val):
            return False

        if self.__validate_bst(node.left, min_val, node.val) is False:
            return False

        if self.__validate_bst(node.right, node.val, max_val) is False:
            return False

        return True


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = ListNode(val)
        else:
            crawler = self.head
            while crawler.next is not None:
                crawler = crawler.next
            crawler.next = ListNode(val)

    def __str__(self):
        vals = ''
        crawler = self.head
        while crawler.next is not None:
            vals += '{}, '.format(crawler.val)
            crawler = crawler.next
        vals += '{}, '.format(crawler.val)

        return vals


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    tree = BinaryTree()
    # tree.insert(20)
    # tree.insert(10)
    # tree.insert(30)
    # tree.insert(5)
    # tree.insert(15)
    # tree.insert(25)
    # tree.insert(40)
    # tree.insert(1)
    # tree.insert(7)
    # tree.insert(13)
    # tree.insert(17)
    # tree.insert(23)
    # tree.insert(28)
    # tree.insert(35)
    # tree.insert(50)

    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(25)
    # tree.insert(4)
    # tree.insert(3)
    # tree.insert(2)
    tree.insert(1)
    tree.insert(7)
    tree.insert(13)
    tree.insert(17)
    tree.insert(23)
    tree.insert(28)
    tree.insert(35)

    tree.head = BinaryNode(None, None, 20)

    tree.insert(10)
    tree.insert(30)
    tree.insert(40)
    tree.insert(5)
    tree.head.right.left = BinaryNode(None, None, 15)
    # tree.head.left.right = BinaryNode(None, None, 25)



    # tree.head.right = BinaryNode(tree.head.right.left, tree.head.right.right, 1)

    print(tree.head.left, '\n')

    # print(tree.get_depth())

    returned_lists = tree.list_per_depth()

    for single_list in returned_lists:
        print(single_list)
    #
    # print()
    # print(tree.balanced())

    print(tree.validate_bst())

    tree.print_in_order()
    # tree.print_pre_order()
    # tree.print_post_order()
    # print(tree.get_sorted())
    # tree.rebalance_tree()
    # tree.print_in_order()
    # print(tree.head.left)
    # print(tree.head.right)
    # print(tree.head.right)


