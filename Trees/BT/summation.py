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

    def max_sum_max_le_utility(self, root, curr_length, max_length, max_sum, sum):
        if root and root.key == 6:
            print '***' , max_length , max_sum , '\n'
        if max_length[0] < curr_length:
            max_sum[0] = sum
            max_length[0] = curr_length
        elif max_length[0] == curr_length:
            max_sum[0] = max(max_sum[0], sum)
        if root:
            print 'updated ' , root.key, max_length , max_sum , '\n'
        if not root:
            print 'None' , max_length , max_sum,  '\n'
            return

        self.max_sum_max_le_utility(root.left , curr_length + 1, max_length, max_sum, sum + root.key)
        self.max_sum_max_le_utility(root.right, curr_length + 1, max_length, max_sum, sum + root.key)

    def check(self, l ,root , count):
        # print l , '\n'
        if not root:
            return
        print root.key, l, '\n'
        l = [count] # Now this l refers to something else

        self.check(l , root=root.left , count=count + 1)
        self.check(l , root=root.right , count=count + 1)

    def max_sum_max_length(self, root):
        max_length = [-100000000000] # for passing through the reference
        max_sum = [-100000000] # for passing through the reference
        self.max_sum_max_le_utility(root, 0 , max_length, max_sum ,0)

        return max_sum[0]

if __name__ == '__main__':

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
    n3.left = n6
    n3.right = n7
    n2.right = n5

    tree = BinaryTree(root=n1)  # n1 as a root
    print tree.max_sum_max_length(tree.root)
    # l = [0]
    # tree.check(l, root=tree.root , count=1)
    # print 'Final ' , l