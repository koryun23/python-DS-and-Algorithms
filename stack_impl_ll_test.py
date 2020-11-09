import unittest
from stack_impl_using_linkedlists import Stack
from linkedlist import LinkedList


class Test(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertTrue(stack.peek()['value'] ==5)


    def test_pop(self):
        stack = Stack()
        stack.push(5)
        stack.push(10)
        stack.pop()
        self.assertTrue(stack.peek()['value'] == 5)
