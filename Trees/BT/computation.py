class TreeNode:
    '''
    This is a tree Node class
    '''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinaryTree():
    '''
    This is a Binary Tree Class
    '''
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

    def is_leaf(self, root):
        if root.right or root.left:
            return False
        return True

    def children_sum(self, root):
        if not root :
            return True

        lr = self.children_sum(root.left)
        rr = self.children_sum(root.right)
        current_result = False
        ls = rs = 0
        if root.left:
            ls = root.left.key
        if root.right:
            rs = root.right.key
        if (ls + rs == root.key) or self.is_leaf(root):
            current_result = True
        return (current_result and lr and rr)

    def sum_tree(self, root):
        if not root:
            return (True , 0)
        lr, ls = self.sum_tree(root.left)
        rr , rs = self.sum_tree(root.right)

        result = False
        if root.key == ls + rs or self.is_leaf(root):
            result = True
        return (result and lr and rr , ls + rs + root.key)




if __name__ == '__main__':
    # n1 = TreeNode(10)  # root
    # n2 = TreeNode(8)
    # n3 = TreeNode(2)
    # n4 = TreeNode(5)
    # n5 = TreeNode(3)
    # n6 = TreeNode(1) # This is for children Sum
    # n7 = TreeNode(1)
    # n8 = TreeNode(8)

    n1 = TreeNode(26)  # root
    n2 = TreeNode(10)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(6)
    n6 = TreeNode(1)
    n7 = TreeNode(2)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    tree = BinaryTree(root=n1)  # n1 as a root
    print tree.children_sum(root=tree.root)
    print "\n"
    print tree.sum_tree(root=tree.root)
