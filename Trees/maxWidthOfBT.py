# Python program to find the maximum width of binary tree using Level Order Traversal with queue.

# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxWidthOfBT(node):
    if not node:
        return 0

    maxWidth = 0
    queue = []
    queue.append(node)
    while len(queue)>0:
        count = len(queue)
        maxWidth = max(count, maxWidth)
        while count > 0:
            count -= 1
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return maxWidth

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(8)
# root.right.right.left = Node(6)
# root.right.right.right = Node(7)

"""
Constructed binary tree is:
       1
      / \
     2   3
    / \   \
   4   5   8
          / \
         6   7
"""
# root = None
print "Maximum width is " + str(maxWidthOfBT(root))
