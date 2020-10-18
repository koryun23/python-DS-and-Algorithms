class DoublyLinkedList:
    def __init__(self, value):
        self.length = 1
        self.head = {
            'value' : value,
            'next' : None,
            'prev' : None
        }
        self.tail = self.head
    def create(self):
        self.mydoublyll = {
            'head':self.head,
            'tail':self.tail,
            'length':self.length
        }
        return self.mydoublyll
    def printList(self):
        values = []
        curNode = self.head
        while curNode != None:
            values.append(curNode['value'])
            curNode = curNode['next']
        return values
    def append(self, value):
        node = {
            'value':value,
            'next':None,
            'prev':None
        }
        node['prev'] = self.tail
        self.tail['next'] = node
        self.tail = node        
        self.length+=1
        return self.create()
    def prepend(self, value):
        node = {
            'value':value,
            'next':None,
            'prev':None
        }
        node['next'] = self.head
        self.head['prev'] = node
        self.head = node
        self.length+=1
        return self.create()
    def insert(self, index, value):
        prevNode = None
        curNode = self.head
        node = {
            'value' : value,
            'next' : None,
            'prev':None

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
            node['next'] = curNode
            node['prev'] = prevNode
            prevNode['next'] = node
            self.length+=1


        return self.create()
    def remove(self, index):

        i = 0
        curNode = self.head
        prevNode = None
        while i < index:
            prevNode = curNode
            curNode = curNode['next']
            i += 1
        if prevNode == None:
            self.head = self.head['next']
        else:
            prevNode['next'] = curNode['next']
            curNode = curNode['next']
            curNode['prev'] = prevNode
            self.length-=1
        return self.create()
    def delete_by_value(self, value):
        prevNode = None
        curNode = self.head
        if self.head['value'] == value:
            self.head = self.head['next']
        else:
            prevNode = curNode
            curNode = curNode['next']
            while True: #[1,99,5,2] delete 99, curNode.value = 99, prevNode.value = 1
                if curNode['value'] == value:
                    prevNode['next'] = curNode['next']
                    curNode = curNode['next']
                    curNode['prev'] = prevNode
                    self.length-=1
                    break
                else:
                    prevNode = curNode
                    curNode = curNode['next']



        return self.create()
    def get(self, value):
        curNode = self.head
        while True:
            if curNode['value'] == value:
                return curNode
                
            curNode = curNode['next']

ll = DoublyLinkedList(10)
print(ll.create())
print(ll.append(5))
print(ll.append(2))
print(ll.prepend(1))
print(ll.printList())
print(ll.insert(2,99))
print(ll.printList())
print(ll.remove(1))
print(ll.printList())
print(ll.delete_by_value(99))
print(ll.printList())
print(ll.get(5))
