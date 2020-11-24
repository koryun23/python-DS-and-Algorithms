# from linkedlist import LinkedList
class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = self.head
    
    def printList(self):
        values = []
        curNode = self.head
        while curNode != None:
            values.append(curNode['value'])
            curNode = curNode['next']
        return values
    def append(self, value):
        node = {
            'value' : value,
            'next' : None
        }
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail['next'] = node
            self.tail = node
        self.length += 1
    def prepend(self, value):
        node = {
            'value' : value,
            'next' : None
        }
        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            node['next'] = self.head
            self.head = node
        self.length += 1
    def insert(self, index, value):
        if self.length == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prevNode = None
        curNode = self.head
        node = {
            'value' : value,
            'next' : None
        }
        i = 0
        while i < index:
            prevNode = curNode
            curNode = curNode['next']
            i+=1
        if prevNode == None:
            node['next'] = self.head
            self.head = node
        else:
            if index == self.length:
                return self.append(value)
            node['next'] = curNode
            prevNode['next'] = node
            self.length+=1        
    def remove(self, index):
        i = 0
        curNode = self.head
        prevNode = None
        while i < index:
            prevNode = curNode
            curNode = curNode['next']
            i += 1
        if index == self.length:
            self.tail = curNode
        elif prevNode == None:
            self.head = self.head['next']
        else:
            prevNode['next'] = curNode['next']
            curNode = curNode['next']
            self.length-=1

    def delete_by_value(self, value):
        prevNode = None
        curNode = self.head
        if self.head['value'] == value:
            self.head = self.head['next']
        else:
            prevNode = curNode
            curNode = curNode['next']
            while True:
                if curNode['value'] == value:
                    prevNode['next'] = curNode['next']
                    curNode = curNode['next']
                    self.length-=1
                    break
                else:
                    prevNode = curNode
                    curNode = curNode['next']

    def get(self, value):
        if self.length == 0:
            return
        curNode = self.head
        while True:
            if curNode['value'] == value:
                return curNode
                
            curNode = curNode['next']

    def reverse(self):
        if self.length == 1:
            return self.head
        first = self.head
        second = first['next']
        while second:
            third = second['next']
            second['next'] = first
            first = second
            second = third
        self.head['next'] = None
        self.head = first 
    def get_by_index(self,index):
        curNode = self.head
        while index>0:
            curNode = curNode['next']
            index -= 1
        return curNode
    def remove_all(self):
        self.head = None
        self.head = None
        self.length = 0



class Stack:
    def __init__(self):
        self.ll = LinkedList()
    def peek(self):
        return self.ll.head
    def push(self,value):
        self.ll.prepend(value)
    def pop(self):
        first = self.ll.get_by_index(0)
        self.ll.remove(0)
        return first

    def get(self):
        stack = {
            'top':self.ll.head,
            'bottom':self.ll.tail,
            'length':self.ll.length
        }
        return stack




myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
myStack.push(50)
print(myStack.pop())
print(myStack.get())



        



