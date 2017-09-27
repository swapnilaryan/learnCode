class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    s1 = [root]
    while len(s1)>0:
        if root.left:
            s1.append(root.left)
            root = root.left
        else:
            temp = s1.pop()
            print temp.data

            if(temp.right):
                s1.append(temp.right)
                root = temp.right

root = Node(1)
root.left = Node(2)
root.right = Node(3)

t=root.right
t.right = Node(13)
t.right.left = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)

t = root.left.right
t.left = Node(9)
t.right = Node(11)

inOrder(root)