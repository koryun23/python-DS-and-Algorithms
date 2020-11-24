from queue_impl import Line
from linkedlist import LinkedList
import unittest

class Test(unittest.TestCase):
    def enqueue_test(self):
        ll = LinkedList()
        line = Line()
        self.assertTrue(ll.append(1) == line.enqueue(1))
    def dequeue_test(self):
        ll = LinkedList()
        line = Line()
        self.assertTrue(ll.remove(0) == line.dequeue())

        