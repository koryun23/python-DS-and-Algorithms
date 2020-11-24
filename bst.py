class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        node = {'value':value,'left':None,'right':None}
        if self.root == None:
            self.root = node 
        else:
            
            current = self.root
            while True:
                if value > current['value']:
                    if current['right'] == None:
                        current['right'] = node
                        break
                    else:
                        current = current['right']
                else:
                    if current['left'] == None:
                        current['left'] = node
                        break
                    else:
                        current = current['left']
    def lookup(self,value):
        if self.root == None:
            return
        else:
            current = self.root
            while True:
                if value > current['value']:
                    if current['right'] == None:
                        return None
                    current = current['right']
                elif value < current['value']:
                    if current['left'] == None:
                        return None
                    current = current['left']
                else:
                    return current

    def remove(self,value):
        if not self.root:
            return False
        parent = None
        current = self.root
        while current:
            if value < current['value']:
                parent = current
                current = current['left']
            elif value > current['value']:
                parent = current
                current = current['right']
            elif value == current['value']:

                # 1)no right child
                if current['right'] == None:
                    if parent == None:
                        self.root = current['left']
                    else:
                        if current['value'] < parent['value']:
                            parent['left'] = current['left']
                        elif current['value'] > parent['value']:
                            parent['right'] = current['left']
                # 2) right child that doesnt have a left child
                elif current['right']['left'] == None:
                    current['right']['left'] = current['left']
                    if parent == None:
                        self.root= current['right']
                    else:
                        if parent['value'] > current['value']:
                            parent['left'] = current['right']
                        elif parent['value'] < current['value']:
                            parent['right'] = current['right']
                # 3)Right child that has a left child
                else:
                    #finding the right child's leftmost child
                    leftmost = current['right']['left']
                    leftmostParent = current['right']
                    while leftmost['left'] != None:
                        leftmostParent = leftmost
                        leftmost = leftmost['left']
                    leftmostParent['left'] = leftmost['right']
                    leftmost['left'] = current['left']
                    leftmost['right'] = current['right']

                    if parent == None:
                        self.root = leftmost
                    else:
                        if current['value'] < parent['value']:
                            parent['left'] = leftmost
                        elif current['value'] > parent['value']:
                            parent['right'] = leftmost
                return True  

    def get(self):
        my_bst = {
            'root':self.root,
        }
        return my_bst
    
    def breadthFirstSearch(self):
        currentNode = self.root
        arr = []
        q = []
        q.append(currentNode)
        while len(q) > 0:
            currentNode = q[0]
            del q[0]
            arr.append(currentNode['value'])
            if currentNode['left']:
                q.append(currentNode['left'])
            if currentNode['right']:
                q.append(currentNode['right'])
        return arr
    def recursiveBFS(self,q,arr):
        if not len(q):
            return arr
        curNode = q[0]
        del q[0]
        arr.append(curNode['value'])
        if curNode['left']:
            q.append(curNode['left'])
        if curNode['right']:
            q.append(curNode['right'])
        return self.recursiveBFS(q,arr)
    def DFS_inorder(self, root,arr):
        if root['left']:
            self.DFS_inorder(root['left'],arr)
        arr.append(root['value'])
        if root['right']:
            self.DFS_inorder(root['right'],arr)
        return arr
    def DFS_preorder(self,root,arr):
        arr.append(root['value'])
        if root['left']:
            self.DFS_preorder(root['left'],arr)
        if root['right']:
            self.DFS_preorder(root['right'],arr)
        return arr
    def DFS_postorder(self,root,arr):
        
        if root['left']:
            self.DFS_postorder(root['left'],arr)
        
        if root['right']:
            self.DFS_postorder(root['right'],arr)
        arr.append(root['value'])
        return arr

        
#           9
#       4        20
#     1   6   15    170


        

    
    

        
bst = BinarySearchTree()
bst.insert(9)
bst.insert(4) 
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)



print('BFS:',bst.breadthFirstSearch())
print('recursive BFS:',bst.recursiveBFS([bst.root],[]))
print('recursive DFS inorder:',bst.DFS_inorder(bst.root, []))
print('recursive DFS preorder:',bst.DFS_preorder(bst.root, []))
print('recursive DFS postorder:',bst.DFS_postorder(bst.root, []))



