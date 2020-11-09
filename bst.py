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
    def recursiveDFS(self, root):
        print(root['value'])
        currentNode = root
        if currentNode['left']:
            self.recursiveDFS(currentNode['left'])
        if currentNode['right']:
            self.recursiveDFS(currentNode['right'])
        
    def filling_q(self, root):
        q = []
        if root:
            if root['left']:
                q.append(root['left']['value'])
            if root['right']:
                q.append(root['right']['value'])
            arr = q
            return q
    def recursiveBFS(self,root):
        if root == self.root:
            print(root['value'])
        que = self.filling_q(root)
        if que:
            for i in range(len(que)):
                print(que[i])
            self.recursiveBFS(root['left'])
            self.recursiveBFS(root['right'])


        
bst = BinarySearchTree()
bst.insert(9)
bst.insert(4) 
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
bst.insert(150)


print('BFS:',bst.breadthFirstSearch())
print('recursive DFS')
bst.recursiveDFS(bst.root)
print('recursive BFS')
bst.recursiveBFS(bst.root)
# bst.remove(20)
# bst.remove(9)
# bst.remove(1)
# bst.remove(170)
# bst.remove(4)
# bst.remove(6)
# bst.remove(15)
# bst.remove(150)

print(bst.get())

