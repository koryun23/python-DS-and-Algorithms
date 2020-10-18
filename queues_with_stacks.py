from stack_impl_using_linkedlists import Stack
class Queue:
    def dequeue(self):
        stack = Stack()
        stack.pop()
    def peek(self):
        stack = Stack()
        return stack.top
    def enqueue(self,value):
        stack = Stack()
        if stack.length == 0:
            node = {
                'value':value,
                'next' : None
            }
            stack.top = node
            stack.bottom = node
        else:
            stack.push(value)
            curNode = stack.top
            stack.top = curNode['next']
            stack.bottom = curNode
