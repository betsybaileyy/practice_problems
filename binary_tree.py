"""reverse the order of values in a binary search tree"""

# init the binary tree node class
class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# init the BST
class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.length = 0
    
    #printing out the breadth first search
    def print_bfs(self):
        if not self.root:
            return

        # set up the queue as the root
        queue = [self.root]

        # iterate through the queue as while greater than 0
        while len(queue) > 0:

            # remove the current node from the queue
            curr_node = queue.pop(0)
            print(curr_node.data)

            # increment the length by one
            self.length += 1

            # if a left node exists, add to queue
            if curr_node.left:
                queue.append(curr_node.left)
            
            # if a right node exists, add to queue
            if curr_node.right:
                queue.append(curr_node.right)


    # print the reversed tree
    def print_reverse(self):
        print("Reverse")

        # if the tree is empty, exit
        if not self.root:
            return

        # queue begins with root
        queue = [self.root]

        # while the queue is not empty
        while len(queue) > 0:

            # remove the current node from the queue
            curr_node = queue.pop(0)
            print(curr_node.data)

            # if both right and left node exist ....
            if curr_node.right and curr_node.left:

                # create temp_right node to store the right node
                temp_right = curr_node.right
                # create temp_left node to store the left node
                temp_left = curr_node.left

                # set temp_right equal to the left node
                curr_node.left = temp_right
                # set temp_left equal to the right node
                curr_node.right = temp_left

                # add both of them to the queue
                queue.append(curr_node.left)
                queue.append(curr_node.right)
                
            else:
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right) 


if __name__ == "__main__":
    # bst = BinarySearchTree()
    tree = BinarySearchTree()
    # Test Case 1
    tree.root = BinaryTreeNode(7)

    tree.root.left = BinaryTreeNode(3)
    tree.root.right = BinaryTreeNode(9)

    tree.root.left.left = BinaryTreeNode(1)
    tree.root.left.right = BinaryTreeNode(5)
    
    tree.print_bfs()
    tree.print_reverse()


   