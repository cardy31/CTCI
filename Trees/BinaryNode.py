class BinaryNode:

    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val
        self.visited = False

    def __str__(self):
        return '[val = {}, right = {}, left = {}]'.format(self.val, self.right, self.left)
