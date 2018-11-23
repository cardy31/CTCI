def main():

    queue = MyQueue()
    queue.push(4)
    queue.push(5)
    queue.push(6)
    queue.print_queue()


class MyQueue:
    def __init__(self):
        self.main = []
        self.stack2 = []

    def push(self, element):
        self.main.append(element)

    def pop(self):
        for i in range(0, len(self.main)):
            self.stack2.append(self.main.pop())

        retval = self.stack2.pop()

        for i in range(0, len(self.stack2)):
            self.main.append(self.stack2.pop())

        return retval

    def print_queue(self):
        print(self.main)


if __name__ == '__main__':
    main()
