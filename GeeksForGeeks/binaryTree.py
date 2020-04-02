class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    def __str__(self):
        return str(self.val)

    def addVal(self, v):
        if v <= self.val:
            if self.left:
                self.left.addVal(v)
            else:
                self.left = Node(v)
        else:
            if self.right:
                self.right.addVal(v)
            else:
                self.right = Node(v)

def inOrderTraversal(node):
    # root left right
    retLst = []
    if node.left:
        retLst.append(inOrderTraversal(node.left))
    retLst.append(node.val)
    if node.right:
        retLst.append(inOrderTraversal(node.right))
    return ' '.join([str(x) for x in retLst])

def preOrderTraversal(node):
    # root left right
    retLst = []
    retLst.append(node.val)
    if node.left:
        retLst.append(preOrderTraversal(node.left))
    if node.right:
        retLst.append(preOrderTraversal(node.right))
    return ' '.join([str(x) for x in retLst])

def postOrderTraversal(node):
    # root left right
    retLst = []
    if node.left:
        retLst.append(postOrderTraversal(node.left))
    if node.right:
        retLst.append(postOrderTraversal(node.right))
    retLst.append(node.val)
    return ' '.join([str(x) for x in retLst])

def maxDepth(node):
    if node is None:
        return 0
    else:
        leftDepth = maxDepth(node.left)
        rightDepth = maxDepth(node.right)
        return max([leftDepth, rightDepth]) + 1 # depth of left tree plus depth of current node, 1
    

if __name__ == '__main__':
    treeVals = [3,5,6,4,7]
    root = Node(4)
    [ root.addVal(i) for i in treeVals ]
    print(inOrderTraversal(root))
    print(preOrderTraversal(root))
    print(postOrderTraversal(root))
    print("Depth:", maxDepth(root))