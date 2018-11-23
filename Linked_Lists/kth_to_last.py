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

    head = kth_to_last(head, 2)

    print("New list:")
    util.print_linked_list(head)


def kth_to_last(head, k):
    if k == 0:
        return head

    crawler1 = head
    crawler2 = head
    count = 0

    while crawler1.next is not None:
        if count >= k:
            crawler2 = crawler2.next

        crawler1 = crawler1.next
        count += 1

    return crawler2


if __name__ == '__main__':
    main()
