class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
root = Node(20)
root.right = Node(30)
root.left = Node(10)
root.left.left = Node(5)
root.left.right = Node(15)
root.left.right.right = Node(17)
root.left.left.left = Node(3)
root.left.left.right = Node(7)

root1 = Node(20)
root1.right = Node(30)
root1.left = Node(10)
root1.left.left = Node(5)
root1.left.right = Node(15)
root1.left.right.right = Node(17)
root1.left.left.left = Node(9)
root1.left.left.right = Node(7)

def isBST(node):
    return _isBST(node,None,None)

def _isBST(node,min,max):
    if node == None:
        return True
    if ((min != None and node.data <= min) or (max != None and node.data > max)):
        return False
    if ((_isBST(node.left , min, node.data) == False) or (_isBST(node.right,node.data,max)== False)):
        return False
    return True
print(isBST(root))
print(isBST(root1))