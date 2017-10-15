# Python program to reverse a linked list in group of given size

# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        prev = None
        while (head != None and k > 0):
            next = head.next
            head.next = prev
            prev = head
            head = next
            k -= 1
        return prev

    def reverseKGroup(self, head, k):
        tempNode = Node(0)
        tempNode.next = head
        tempHead = head
        prev = tempNode

        while tempHead:
            # Starting of each reversed list, it will become the last after reversing
            klast = tempHead
            num = k
            # Jump k
            while num > 0 and tempHead is not None:
                tempHead = tempHead.next
                num -= 1
            # If cannot reverse
            if num != 0:
                prev.next = klast
                break

            # start of each reversed group
            kstart = self.reverse(klast, k)

            # use previous's next to point to curr reversed
            prev.next = kstart

            # Set prev to current rev end.
            prev = klast
            llist.head = tempNode.next
            llist.printList()

        return tempNode.next

        # Function to insert a new node at the beginning

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next
        print "\n"


# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print "Given linked list"
llist.printList()
llist.head = llist.reverseKGroup(llist.head, 4)
print "\nReversed Linked list"
llist.printList()
