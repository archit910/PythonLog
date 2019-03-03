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


if __name__ == "__main__":

    n1 = TreeNode(1) #root
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n3.right = n4
    tree = BinaryTree(n1) #n1 as a root
    tree.preorderR(tree.root)
    print "\n"
    tree.inorderR(tree.root)




