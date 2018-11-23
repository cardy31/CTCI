class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        if self.__stack:
            return True
        return False

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]
