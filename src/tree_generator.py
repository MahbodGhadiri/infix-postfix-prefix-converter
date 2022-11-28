from structures.Stack import Stack
from structures.Tree import Tree

def generate(postfix):
    stack = Stack()
    for c in postfix:
        if c.isalnum():
            stack.push(c)
        else:
            right = stack.pop()
            if(isinstance(right,str)):
                right = Tree(right, None, None)
            left = stack.pop()
            if(isinstance(left,str)):
                left = Tree(left, None, None)
            tree = Tree(c, left, right)
            stack.push(tree)
    return stack.pop()


def evaluateExpressionTree(root: Tree):
    # empty tree
    if root is None:
        return 0
    
    if isinstance(root, str):
        return root
    # leaf node
    if root.left is None and root.right is None:
        return root.data
 
    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)
 
    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)
 
    # check which operation to apply
    return "("+ left_sum + root.data + right_sum + ")"
 




