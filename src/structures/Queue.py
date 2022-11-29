class Queue:
    def __init__(self):
        self.q = []
    
    def pop(self):
        return self.q.pop(0)
    
    def add(self, data):
        self.q.append(data)

    def isEmpty(self)->bool:
        return len(self.q) == 0