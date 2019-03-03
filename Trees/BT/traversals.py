class TreeNode:
    '''
    This is a tree class
    '''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinaryTree():

    def __init__(self, root):
        self.root = root

    def preorderR(self, root):
        if not root:
            return
        print root.key,
        self.preorderR(root.left)
        self.preorderR(root.right)

    def inorderR(self, root):
        if not root:
            return
        self.inorderR(root.left)
        print root.key,
        self.inorderR(root.right)

    def postorderR(self, root):
        if not root:
            return
        self.postorderR(root.left)
        self.postorderR(root.right)
        print root.key

    def levelorderQ(self, root):
        #level order traversal using Queue
        queue = []
        queue.append(root)
        while queue:
            front_node = queue[0]
            if front_node.left:
                queue.append(front_node.left)
            if front_node.right:
                queue.append(front_node.right)
            print front_node.key,
            queue.pop(0)

    def reverse_level_order(self, root):
        '''
        This function prints a tree in reverse order
        '''
        queue = []
        stack = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            stack.append(node)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        while stack:
            root = stack.pop()
            print root.key

    def diagnal_traversal_utility(self, root, levels, hd):
            #preorder traversal
            if hd in levels:
                levels[hd].append(root)
            else:
                levels[hd] = list()


    def diagonal_traversal(self,root):
        levels = dict()
        self.diagnal_traversal_utility(root,levels, 0)




if __name__ == '__main__':

    n1 = TreeNode(1)  # root
    n2 = TreeNode(3)
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n1.left = n2
    n1.right = n3
    n3.right = n4
    tree = BinaryTree(n1)  # n1 as a root
    tree.preorderR(root=tree.root)
    print '\nLevel Order Traversal is \n'
    tree.levelorderQ(root=tree.root)


