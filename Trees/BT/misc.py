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

    def is_leaf(self, root):
        if root.right or root.left:
            return False
        return True

    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.right) + self.count(root.left)

    def get_lca(self, root, key1, key2):
        if not root:
            return None
        if root.key == key1 or root.key == key2:
            return root
        l_side = self.get_lca(root.left, key1, key2)
        r_side = self.get_lca(root.right, key1, key2)

        if l_side and r_side:
            return root
        value = l_side or r_side
        return value

    def is_bst_utilty(self, root, flags):
        if not root:
            return

        self.is_bst_utilty(root.left, flags)
        # do stuff
        if flags.get('prev') > root.key:
            flags['is_bst'] = False
        flags['prev'] = root.key

        self.is_bst_utilty(root.right, flags)

    def is_bst(self, root):
        flags = {'prev' : -10,
                 'is_bst': True}
        self.is_bst_utilty(root,flags)
        return flags.get('is_bst')


if __name__ == '__main__':
    n1 = TreeNode(26)  # root
    n2 = TreeNode(10)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(6)
    n6 = TreeNode(1)
    n7 = TreeNode(13)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    tree = BinaryTree(root=n1)  # n1 as a root
    # lca = tree.get_lca(tree.root, 6, 3)
    # print lca.key
    printtre