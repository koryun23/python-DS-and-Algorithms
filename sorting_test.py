import unittest
import bubble_sort
import selection_sort
import insertion_sort
import merge_sort
import quick_sort

class Test_Sorting(unittest.TestCase):

    def bubble_sort_test(self):
        self.assertTrue(bubble_sort.bubble_sort([45,2,5,6,31,5]) == [2,5,5,6,31,45])

    def selection_sort_test(self):
        self.assertTrue(selection_sort.selection_sort([45,2,5,6,31,5]) == [2,5,5,6,31,45])

    def insertion_sort_test(self):
        self.assertTrue(insertion_sort.insertion_sort([45,2,5,6,31,5]) == [2,5,5,6,31,45])

    def merge_sort_test(self):
        self.assertTrue(merge_sort.merge_sort([45,2,5,6,31,5]) == [2,5,5,6,31,45])

    def quick_sort_test(self):
        self.assertTrue(quick_sort.quick_sort([45,2,5,6,31,5],0,5) == [2,5,5,6,31,45])
        self.assertTrue(quick_sort.quick_sort([45,2,5,6,31,5],1,5) == [45,2,5,5,6,31])
        self.assertTrue(quick_sort.quick_sort([45,2,5,6,31,5],0,4) == [2,5,6,31,45,5])
    