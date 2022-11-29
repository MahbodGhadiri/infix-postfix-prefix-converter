from structures.Stack import Stack
from structures.Tree import Tree

def generate(postfix):
    stack = Stack()
    depth: int = 0
    for c in postfix:
        if c.isalnum():
            stack.push(c)
        else:
            right = stack.pop()
            if(isinstance(right,str)):
                right = Tree(right)
            left = stack.pop()
            if(isinstance(left,str)):
                left = Tree(left)
            tree = Tree(c, left, right)
            depth += 1
            stack.push(tree)
    return [stack.pop(), depth]



