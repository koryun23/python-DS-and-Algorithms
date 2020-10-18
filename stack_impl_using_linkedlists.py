from linkedlist import LinkedList
class Stack:
    def __init__(self):
        ll = LinkedList()
        self.top = ll.head
        self.bottom = ll.tail
        self.length = ll.length
    def peek(self):
        ll = LinkedList()
        return ll.head
    def push(self,value):
        ll = LinkedList()
        ll.prepend(value)
    def pop(self):
        ll = LinkedList()
        ll.remove(0)



    # def __init__(self):
    #     self.top = None
    #     self.bottom = self.top
    #     self.length = 0
    # def getStack(self):
    #     stack = {
    #         'top':self.top,
    #         'bottom':self.bottom,
    #         'length':self.length
    #     }
    #     return stack
    # def peek(self):
    #     return self.top
    # def push(self,value):
    #     node = {
    #         'value':value,
    #         'next':None
    #     }
    #     if self.length == 0:
    #         self.bottom = node
    #         self.top = node
    #     else:
    #         curNode = self.top
    #         self.top = node
    #         self.top['next'] = curNode
    #     self.length+=1
    #     return self.getStack()
    # def pop(self):
    #     if self.length == 1:
    #         self.top = None
    #         self.bottom = None
    #         self.length -= 1
    #     else:
    #         self.top = self.top['next']
    #         self.length -= 1
    #     return self.getStack()




# myStack = Stack()
# print(myStack.getStack())
# myStack.push(10)
# print(myStack.getStack())
# myStack.push(15)
# print(myStack.getStack())
# myStack.push(20)
# print(myStack.getStack())
# myStack.pop()
# print(myStack.getStack())
# myStack.pop()
# print(myStack.getStack())
# myStack.pop()
# print(myStack.getStack())
# print(myStack.peek())


# myStack.push(20)
# print(myStack.getStack())
# print(myStack.peek())



