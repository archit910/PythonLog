import copy

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
    
    def is_child(self,root):
        if root.left == None and root.right == None:
            return True
        return False
    
    def equal_sum_utility(self, root, ans):
        if not root:
            return 0
        lr = self.equal_sum_utility(root.left, ans)
        rr = self.equal_sum_utility(root.right, ans)
        if root.key != lr + rr and not self.is_child(root):
            ans[0] = False
        return root.key + lr + rr
    
    def equal_sum(self, root):
        ans = [True]
        self.equal_sum_utility(root, ans)
        return ans[0]


if __name__ == '__main__':
    # n1 = TreeNode(10)  # root
    # n2 = TreeNode(8)
    # n3 = TreeNode(2)
    # n4 = TreeNode(5)
    # n5 = TreeNode(3)
    # n6 = TreeNode(1) # This is for children Sum
    # n7 = TreeNode(1)
    # n8 = TreeNode(8)
    n1 = TreeNode(24)  # root
    n2 = TreeNode(3)
    n3 = TreeNode(9)
    n4 = TreeNode(1)
    n5 = TreeNode(2)
    n6 = TreeNode(4)
    n7 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5 # comment it to split a tree into two halves
    n3.left = n6
    n3.right = n7

    tree =  BinaryTree(root= n1)
    r = tree.equal_sum(root = tree.root)
    print 'Equal Tree : ' ,r
