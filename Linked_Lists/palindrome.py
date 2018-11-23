from Linked_Lists.Node import Node
from Linked_Lists.Main import LinkedListUtility


def main():
    util = LinkedListUtility()

    list1 = Node(1)
    util.add_node(list1, new_node=Node(2))
    util.add_node(list1, new_node=Node(0))
    util.add_node(list1, new_node=Node(1))
    util.add_node(list1, new_node=Node(1))

    print(palindrome(list1))


# Runtime is O(2n) == O(n)
def palindrome(head):
    if head.next is None:
        return True

    list_len = 1

    crawler = head

    while crawler.next is not None:
        list_len += 1
        crawler = crawler.next

    stack = []
    crawler = head

    # Even
    if list_len % 2 == 0:
        for i in range(0, int(list_len / 2)):
            stack.append(crawler.val)
            crawler = crawler.next
        for i in range(int(list_len / 2), list_len):
            if crawler.val != stack.pop():
                return False
            crawler = crawler.next
        return True

    # Odd
    for i in range(0, int((list_len - 1) / 2)):
        stack.append(crawler.val)
        crawler = crawler.next
    crawler = crawler.next

    for i in range(int((list_len - 1) / 2) + 2, list_len):
        if crawler.val != stack.pop():
            return False
        crawler = crawler.next
    return True


if __name__ == '__main__':
    main()
