class Stack:
    def __init__(self):
        self.stack = []
    def peek(self):
        if len(self.stack) == 0:
            return 
        return self.stack[-1]
    def push(self,value):
        self.stack.append(value)
        return self.stack
    def pop(self):
        self.stack.pop()
        return self.stack
myStack = Stack()
print(myStack.peek())
print(myStack.push(10))
print(myStack.push(5))
print(myStack.pop())
print(myStack.peek())

