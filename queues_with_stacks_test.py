from queues_with_stacks import Queue
from queue_impl import Line
import unittest

class Test_Queues(unittest.TestCase):
    def enqueue_test(self):
        queue = Line()
        queue_stack = Queue()
        self.assertTrue(queue.enqueue(1) == queue_stack.enqueue(1))


