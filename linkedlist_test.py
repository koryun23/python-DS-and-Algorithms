from linkedlist import LinkedList 
import unittest



class Test_LinkedList(unittest.TestCase):
    def test_create(self):
        ll = LinkedList()
        self.assertTrue(len(ll.printList()) == 0)
        

    def test_append(self):
        ll = LinkedList()
        ll.append(5)
        self.assertTrue(len(ll.printList())==1)
        self.assertTrue(ll.printList()[0] == 5)
    def test_prepend(self):
        ll = LinkedList()
        ll.append(5)
        ll.prepend(1)
        self.assertTrue(len(ll.printList())== 2)
        self.assertTrue(ll.printList()[0] == 1)
    def test_remove(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(16)
        ll.prepend(1)
        ll.remove(2)
        ll.append(5)
        self.assertTrue(len(ll.printList()) == 2)
        self.assertTrue(ll.printList()[1] == 5)


    def test_insert(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(16) #[10,5,16]
        ll.prepend(1)
        ll.insert(3, 4)
        ll.append(5)
        self.assertTrue(ll.printList()[3] == 4)
        self.assertTrue(len(ll.printList()) == 5)
        self.assertTrue(ll.printList() == [1,5,16,4,5])
    def test_delete_by_value(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(16)
        ll.prepend(1)
        ll.delete_by_value(16)
        self.assertTrue(ll.printList()[1] == 5)
        self.assertTrue(len(ll.printList()) == 2)
    def test_get(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(16)
        self.assertTrue(ll.get(5)['value'] == 5)
    def test_reverse(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(16)
        ll.append(25)
        ll.append(41)
        ll.reverse()
        self.assertTrue(ll.printList() == [41,25,16,5])
    def get_by_index_test(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(16)
        ll.append(35)
        ll.append(67)
        self.assertTrue(ll.get_by_index(2) == ll.printList()[2])
        self.assertTrue(ll.get_by_index(2)['value'] == 35)
    def remove_all_test(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(16)
        ll.append(35)
        ll.append(67)
        self.assertTrue(ll.length == 4 and ll.head['value'] == 5)
        ll.remove_all()
        self.assertTrue(ll.length ==0 and ll.head == None)
    



