class Tree:
    data = None
    left = None
    right = None

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
