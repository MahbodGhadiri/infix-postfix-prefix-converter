from structures.Stack import Stack

class Converter:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def hasPrecedent(self, operator1: str, operator2: str):
        if operator2 == "(":
            return True
        return (self.precedence[operator1] > self.precedence[operator2])
        

    def reverse(self, string: str) -> str:
        s = ""
        for c in reversed(string):
            if c == "(":
                s += ")"
            elif c == ")":
                s += "("
            else:
                s += c
        return s


    def infix_to_postfix(self, infix):
        postfix = ""
        stack = Stack()
        for c in infix:
            if(c.isalnum()):
                postfix += c
            elif c == "(":
                stack.push(c)
            elif c == ")":
                while True:
                    operator = stack.pop()
                    if operator == "(":
                        break
                    else:
                        postfix += operator
            else:
                while((not stack.isEmpty()) and (not self.hasPrecedent(c, stack.getTop()))):
                    postfix += stack.pop()
                stack.push(c)
        while(not stack.isEmpty()):
            postfix += stack.pop()
        return postfix


    def infix_to_prefix(self, infix):
        print(1,infix)
        prefix = self.reverse(infix)
        print(2,prefix)
        prefix = self.infix_to_postfix(prefix)
        print(3,prefix)
        prefix = self.reverse(prefix)
        print(4,prefix)
        return prefix

    def postfix_to_infix(self, postfix: str) -> str:
        stack = Stack()
        for c in postfix:
            if c.isalnum():
                stack.push(c)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.push("("+operand1+c+operand2+")")
        return stack.pop()
    
    def postfix_to_prefix(self, postfix: str) -> str:
        stack = Stack()
        for c in postfix:
            if c.isalnum():
                stack.push(c)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.push(c+operand1+operand2)
        return stack.pop()

    def prefix_to_infix(self, prefix: str) -> str:
        infix = self.reverse(prefix)
        infix = self.postfix_to_infix(infix)
        infix = self.reverse(infix)
        return infix

    def prefix_to_postfix(self, prefix: str) -> str:
        postfix = self.reverse(prefix)
        postfix = self.postfix_to_prefix(postfix)
        postfix = self.reverse(postfix)
        return postfix


    