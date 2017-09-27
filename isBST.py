# Python program to check if a binary tree is bst or not

INT_MAX = 4294967296
INT_MIN = -4294967296


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(node, l=None, r=None):
    if node is None:
        return True

    if l is not None and l.data > node.data:
        return False

    if r is not None and r.data < node.data:
        return False

    return isBST(node.left, l, node) and isBST(node.right, node, r)


# Driver program to test above function
root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)

if isBST(root):
    print "Is BST"
else:
    print "Not a BST"

