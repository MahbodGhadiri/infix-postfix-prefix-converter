from structures.Stack import Stack

class Converter:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = ['-','+','*','/','^']

    def preHasPrecedent(self, operator1: str, operator2: str):
        if operator2 == "(":
            return True
        if(operator1=="^" and operator2=="^"):
            return False
        return (self.precedence[operator1] <= self.precedence[operator2])

    def postHasPrecedent(self, operator1: str, operator2: str):
        if operator2 == "(":
            return True
        if(operator1=="^" and operator2=="^"):
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
                while((not stack.isEmpty()) and (not self.postHasPrecedent(c, stack.getTop()))):
                    postfix += stack.pop()
                stack.push(c)
        while(not stack.isEmpty()):
            postfix += stack.pop()
        return postfix


    def infix_to_prefix(self, infix):
        operators = Stack()
        operands = Stack()
        for c in infix:
            if c == "(":
                operators.push(c)
            elif c == ")":
                while (not operators.isEmpty() and (operators.getTop()!="(")):
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    operator = operators.pop()
                    operands.push(operator+operand2+operand1)
                operators.pop() # removing "("
            elif c.isalnum():
                operands.push(c)
            else:
                while (not operators.isEmpty() and self.preHasPrecedent(c, operators.getTop()) and (operators.getTop()!="(")):
                    operand1 = operands.pop()
                    operand2 = operands.pop()
                    operator = operators.pop()
                    operands.push(operator+operand2+operand1)
                operators.push(c)
        while not operators.isEmpty():
            operand1 = operands.pop()
            operand2 = operands.pop()
            operator = operators.pop()
            operands.push(operator+operand2+operand1)
        return operands.pop()

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
        stack = Stack()
        prefix = self.reverse(prefix)
        for c in prefix:
            # if c is an operand
            if(c.isalnum()):
                stack.push(c)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.push(operand1+operand2+c)
        return stack.pop()

    def detectMode(self, expression: str) -> str:
        # check for prefix
        for c in expression:
            if c != '(':
                if not c.isalnum():
                    return "Prefix"
                break
        #check for postfix
        expression = expression[::-1]
        for c in expression:
            if c != ")":
                if not c.isalnum():
                    return "Postfix"
                break

        return "Infix"

    def validateExpression(self, expression):
        operatorsCount = 0
        operandsCount = 0
        openParenthesis = 0
        for c in expression:
            if c == "(":
                openParenthesis += 1
            elif c == ")":
                if openParenthesis > 0:
                    openParenthesis -= 1
                else:
                    raise "Wrong parenthesis"
            elif c.isalnum():
                operandsCount += 1
            else:
                if c in self.operators:
                    operatorsCount += 1
                else:
                    raise "unsupported operator"
        if openParenthesis != 0:
            raise "Wrong parenthesis"
        if operandsCount != operatorsCount + 1:
            raise "Invalid expression"
            

'''
simple test cases

a-b-c
a^b^c
abcd^e-fgh*+^*+i-
-+a*b^-^cde+f*ghi
a+b*(c^d-e)^(f+g*h)-i
'''
