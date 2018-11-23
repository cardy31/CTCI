from Linked_Lists.Node import Node
from Linked_Lists.Main import LinkedListUtility


def main():
    util = LinkedListUtility()

    head = Node(3)

    util.add_node(head, new_node=Node(5))
    util.add_node(head, new_node=Node(8))
    util.add_node(head, new_node=Node(5))
    util.add_node(head, new_node=Node(10))
    util.add_node(head, new_node=Node(2))
    util.add_node(head, new_node=Node(1))

    util.print_linked_list(head)

    partition(head, 5)

    print("New list:")
    util.print_linked_list(head)


# Runtime is O(n) since we go over all elements once for the length, and once for the check to move things.
# This O(2n) becomes O(n)
def partition(head, part):
    crawl1 = head
    crawl2 = head
    length = 0
    count = 0

    while crawl1.next is not None:
        crawl1 = crawl1.next
        length += 1

    while crawl2.next is not None and count < length:
        if crawl2.val >= part:
            crawl1.next = Node(crawl2.val)
            crawl1 = crawl1.next
            crawl2.val = crawl2.next.val
            crawl2.next = crawl2.next.next
        else:
            crawl2 = crawl2.next
        count += 1


if __name__ == '__main__':
    main()  
