from Linked_Lists.Node import Node
from Linked_Lists.Main import LinkedListUtility


def main():
    util = LinkedListUtility()

    list1 = Node(7)
    util.add_node(list1, new_node=Node(1))
    util.add_node(list1, new_node=Node(0))
    util.add_node(list1, new_node=Node(6))

    list2 = Node(2)
    util.add_node(list2, new_node=Node(9))
    util.add_node(list2, new_node=Node(1))

    print(sum_lists(list1, list2))


# Runtime is O(2n + 2m)
def sum_lists(list1, list2):
    stack1 = []
    stack2 = []

    while list1.next is not None:
        stack1.append(list1.val)
        list1 = list1.next
    stack1.append(list1.val)

    while list2.next is not None:
        stack2.append(list2.val)
        list2 = list2.next
    stack2.append(list2.val)

    number1 = ''
    while len(stack1) > 0:
        number1 += str(stack1.pop())

    number2 = ''
    while len(stack2) > 0:
        number2 += str(stack2.pop())

    return int(number1) + int(number2)


if __name__ == '__main__':
    main()
