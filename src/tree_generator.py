from structures.Stack import Stack
from structures.Tree import Tree

def generate(postfix):
    stack = Stack()
    depth: int = 0
    for c in postfix:
        if c.isalnum():
            tree = Tree(c)
            stack.push(tree)
        else:
            right = stack.pop()
            left = stack.pop()
            depth = left.depth if left.depth > right.depth else right.depth
            tree = Tree(c, left, right, depth=depth+1)
            stack.push(tree)
    return stack.pop()



