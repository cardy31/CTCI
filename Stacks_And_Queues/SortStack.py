def main():

    stack = [10, 50, 45, 37, 56, 1, 30]
    print(stack)
    print(sort_stack(stack))


# Stack supports push, pop, peek, and isempty
def sort_stack(stack):
    stack_sorted = []

    max_val = -100

    while stack:
        temp = stack.pop()
        print_stacks(stack, stack_sorted)

        count = 0

        # If stack is empty
        if not stack_sorted:
            stack_sorted.append(temp)
            continue

        if temp <= stack_sorted[-1]:
            stack_sorted.append(temp)
        else:
            while stack_sorted and temp >= peek(stack_sorted):
                stack.append(stack_sorted.pop())
                count += 1
            stack_sorted.append(temp)
            for i in range(0, count):
                stack_sorted.append(stack.pop())
            count = 0

    return stack_sorted


def print_stacks(s1, s2):
    print('s1: {}\ns2: {}'.format(s1, s2))


def peek(stack):
    return stack[-1]


if __name__ == '__main__':
    main()
