# Python program to reverse a linked list in group of given size

# Node class
class ListNode:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        listLen = self.get_length(head)
        # print listLen
        segments = listLen / k
        dummy = curr = ListNode(0)
        dummy.next = head
        for i in xrange(segments):
            prev = None
            start = head
            for j in xrange(k):
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            # print prev.val
            curr.next = prev
            curr = start
            curr.next = head

            llist.head = dummy.next
            llist.printList()

        return dummy.next

    def get_length(self, head):
        i = 0
        while head:
            head = head.next
            i += 1
        return i


            # Function to insert a new node at the beginning

    def push(self, new_data):
        new_node = ListNode(new_data)
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
# llist.push(9)
# llist.push(8)
# llist.push(7)
# llist.push(6)
# llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print "Given linked list"
llist.printList()
llist.head = llist.reverseKGroup(llist.head, 2)
print "\nReversed Linked list"
llist.printList()
