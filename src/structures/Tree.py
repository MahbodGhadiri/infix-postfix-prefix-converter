class Tree:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
