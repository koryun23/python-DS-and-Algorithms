from bst import BinarySearchTree

def search(arr,value):
    bst = BinarySearchTree
    for i in range(arr):
        bst.insert(arr[i])
    return bst.lookup(value)

print(search([1,4,6,3,8]))