class TernaryNode:

    def __init__(self, val, adjacent):
        self.val = val
        self.adjacent = adjacent
        self.visited = False
        self.marked = False
