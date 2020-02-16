"""
Reverse the order of a singly-linked list by modifying
the nodes links.
"""

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes

    def insert(self, item):
        """Insert the given item at the given index in this linked list."""
        new_node = Node(item)

        # node is now the head of the LL
        node = self.head 

        # if the head is none, set it to the new_node
        if self.head == None:
            self.head = new_node
        
        # otherwise while the node isn't empty
        else:
            while node is not None:
                # if the node's pointer is pointing to none
                if node.next == None:
                    # create the new node
                    node.next = new_node
                    break
                node = node.next
            
    def reverse_ll(self):
        """reverse the nodes of this linked list"""
        # set the current node to be head
        current_node = self.head
        previous_node = None # there is no previous_node yet
        next = None # not pointing to anything

        # while not empty
        while current_node is not None:
            next = current_node.next # current node set to next
            current_node.next = previous_node # the next is now previous
            previous_node = current_node 
            current_node = next

        self.head = previous_node #reset the head to be the previous node



    def show_list(self):
        """print nodes of the linked list"""
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


if __name__ == "__main__":
    list = LinkedList()
    print(list)
    list.insert('A')
    list.insert('B')
    list.insert('C')
    list.insert('D')
    list.insert('E')
    list.insert('F')
    print("----original list----")
    list.show_list()
    list.reverse_ll()
    print("----reversed list----")
    list.show_list()
    print("----yay!----")