class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):
    def insert(self, currNode, val):
        if not currNode:
            return TreeNode(val)
        elif val < currNode.val:
            currNode.left = self.insert(currNode.left, val)
        else:
            currNode.right = self.insert(currNode.right, val)
        
        currNode.height = 1 + max(self.getHeight(currNode.left), self.getHeight(currNode.right))
        balance = self.getBalance(currNode)

        if balance > 1 and val < currNode.left.val:
            return self.rightRotate(currNode)
        elif balance < -1 and val > currNode.right.val:
            return self.leftRotate(currNode)
        elif balance > 1 and val > currNode.left.val:
            currNode.left = self.leftRotate(currNode.left)
            return self.rightRotate(currNode)
        elif balance < -1 and val < currNode.right.val:
            currNode.right = self.rightRotate(currNode.right)
            return self.leftRotate(currNode)

        return currNode

    def leftRotate(self, z):
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, currNode):
        if not currNode:
            return 0
        else:
            return currNode.height

    def getBalance(self, currNode):
        if not currNode:
            return 0
        else:
            return ( self.getHeight(currNode.left) - self.getHeight(currNode.right) )

    def preOrder(self, root):
        if not root: 
            return ''
  
        return(f'{root.val}: [{self.preOrder(root.left)}] [{self.preOrder(root.right)}]') 

if __name__ == '__main__':
    myTree = AVL_Tree() 
    root = None
    
    root = myTree.insert(root, 10) 
    print(myTree.preOrder(root))
    root = myTree.insert(root, 20) 
    print(myTree.preOrder(root))
    root = myTree.insert(root, 30) 
    print(myTree.preOrder(root))
    root = myTree.insert(root, 40) 
    print(myTree.preOrder(root))
    root = myTree.insert(root, 50) 
    print(myTree.preOrder(root))
    root = myTree.insert(root, 25) 

    print(myTree.preOrder(root))