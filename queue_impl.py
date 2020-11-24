from linkedlist import LinkedList
class Line:
    def enqueue(self, value):
        ll = LinkedList()
        ll.append(value)

    def dequeue(self):
        ll = LinkedList()
        ll.remove(0)

    def peek(self):
        ll = LinkedList()
        return ll.head
