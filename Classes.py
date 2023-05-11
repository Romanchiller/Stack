class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) > 0:
            return True
        else:
            return False

    def push(self, el):
        self.data.append(el)
        return

    def pop(self):
        x = self.data.pop()
        return x

    def peek(self):
        x = len(self.data)
        try:
            return self.data[x-1]
        except IndexError:
            return False

    def size(self):
        size = len(self.data)
        return size


