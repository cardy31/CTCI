from Linked_Lists.Node import Node
from Linked_Lists.Main import LinkedListUtility


def main():
    util = LinkedListUtility()

    head = Node(1)

    util.add_node(head, new_node=Node(1))
    util.add_node(head, new_node=Node(1))
    util.add_node(head, new_node=Node(1))
    util.add_node(head, new_node=Node(2))
    util.add_node(head, new_node=Node(2))
    util.add_node(head, new_node=Node(3))

    util.print_linked_list(head)

    head = remove_dups(head)

    print("New list:")
    util.print_linked_list(head)


def remove_dups(head):
    if head is None or head.next is None:
        return head

    crawler = head
    buffer = [head.val]

    while crawler.next is not None:
        if crawler.next.val in buffer:
            crawler.next = crawler.next.next
        else:
            buffer.append(crawler.next.val)
            crawler = crawler.next

    return head


if __name__ == '__main__':
    main()
