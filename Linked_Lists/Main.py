from Linked_Lists.Node import Node


def main():
    util = LinkedListUtility

    head = Node(0)

    util.add_node(head, Node(1))
    util.add_node(head, Node(2))
    util.add_node(head, Node(3))

    util.print_linked_list(head)

    head = util.delete_node(head, 1)

    util.print_linked_list(head)


class LinkedListUtility():
    @staticmethod
    def add_node(head, new_node):
        crawler = head
        if not isinstance(head, Node):
            return False
        while crawler.next is not None:
            crawler = crawler.next

        crawler.next = new_node

    @staticmethod
    def delete_node(head, value):
        if head.val == value:
            return head.next

        crawler = head

        while crawler.next is not None:
            if crawler.next.val == value:
                crawler.next = crawler.next.next
                return head
            crawler = crawler.next
        return head

    @staticmethod
    def print_linked_list(head):
        if head is None or not isinstance(head, Node):
            return False

        crawler = head

        while crawler.next is not None:
            print(crawler.val)
            crawler = crawler.next
        print(crawler.val)
        print()


if __name__ == '__main__':
    main()
