class Stack:
    def __init__(self) -> None:
        self.top = -1
        self.s = []
        self.size = 0

    def pop(self):
        if(self.top>=0):
            self.top -= 1
            return self.s.pop()
        raise Exception("cannot pop from empty stack")

    def push(self, data):
        self.s.append(data)
        self.top +=1

    def getTop(self):
        if(self.top>-1):
            return self.s[self.top]
        return "-"
    def isEmpty(self):
        if(self.top<0):
            return True
        return False



    