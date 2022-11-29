class Tree:

    def __init__(self, data, left = None, right = None, depth = 1):
        self.data = data
        self.left = left
        self.right = right
        self.depth = depth

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
