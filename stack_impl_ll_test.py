import unittest
from stack_impl_using_linkedlists import Stack
from linkedlist import LinkedList


class Test(unittest.TestCase):
    def test_push(self):
        ll = LinkedList()
        stack = Stack()
        self.assertTrue(ll.prepend(1) == stack.push(1))


    def test_pop(self):
        ll = LinkedList()
        stack = Stack()
        self.assertTrue(ll.remove(0) == stack.pop())
