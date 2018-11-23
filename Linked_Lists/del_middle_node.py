from Linked_Lists.Node import Node
from Linked_Lists.Main import LinkedListUtility


def main():
    util = LinkedListUtility()

    head = Node(1)

    util.add_node(head, new_node=Node(2))
    util.add_node(head, new_node=Node(3))
    util.add_node(head, new_node=Node(4))
    util.add_node(head, new_node=Node(5))
    util.add_node(head, new_node=Node(6))

    util.print_linked_list(head)

    crawler = head
    crawler = head.next
    crawler = head.next
    crawler = head.next

    del_middle_node(crawler)

    print("New list:")
    util.print_linked_list(head)


def del_middle_node(node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    main()
