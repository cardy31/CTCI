def main():

    set_of_stacks = SetOfStacks(2)

    print(set_of_stacks.pop())

    set_of_stacks.push(10)
    set_of_stacks.print_all_stacks()
    set_of_stacks.push(3)
    set_of_stacks.push(4)
    set_of_stacks.push(3)
    set_of_stacks.print_all_stacks()
    set_of_stacks.pop()
    set_of_stacks.print_all_stacks()
    set_of_stacks.pop()
    set_of_stacks.print_all_stacks()
    set_of_stacks.pop()
    set_of_stacks.pop()
    set_of_stacks.push(3)
    set_of_stacks.push(4)
    set_of_stacks.print_all_stacks()
    set_of_stacks.print_all_stacks()


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.all_stacks = []
        self.all_stacks.append([])
        print(self.all_stacks)

        self.most_recent_stack = 0

    def push(self, element):
        # Push new element onto most recent stack
        self.all_stacks[self.most_recent_stack].append(element)

        # If the current stack is at capacity, add a new stack and move the most recent stack tracker to there
        if len(self.all_stacks[self.most_recent_stack]) == self.capacity:
            self.all_stacks.append([])
            self.most_recent_stack += 1

    def pop(self):
        # If the current stack is empty
        if len(self.all_stacks[self.most_recent_stack]) == 0:
            # If we have more than one stack
            if len(self.all_stacks) > 1:
                # Remove the empty stack
                self.all_stacks.pop(self.most_recent_stack)
                # Decrement the track of what the most recent stack is
                self.most_recent_stack -= 1
            else:
                # No more stack left
                return 'Error: Nothing left in any stack'
            # Delete last stack

        # Stacks are in a good place, return appropriate element
        most_recent_index = len(self.all_stacks[self.most_recent_stack]) - 1
        return self.all_stacks[self.most_recent_stack].pop(most_recent_index)

    def print_all_stacks(self):
        print(self.all_stacks)


if __name__ == '__main__':
    main()
