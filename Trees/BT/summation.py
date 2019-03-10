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

        if max_length[0] < curr_length:
            max_sum[0] = sum
            max_length[0] = curr_length
        elif max_length[0] == curr_length:
            max_sum[0] = max(max_sum[0], sum)
        if not root:
            return
        self.max_sum_max_le_utility(root.left , curr_length + 1, max_length, max_sum, sum + root.key)
        self.max_sum_max_le_utility(root.right, curr_length + 1, max_length, max_sum, sum + root.key)

    def max_sum_max_length(self, root):
        max_length = [-100000000000] # for passing through the reference
        max_sum = [-100000000] # for passing through the reference
        self.max_sum_max_le_utility(root, 0 , max_length, max_sum ,0)

        return max_sum[0]

    def max_sum_path_utility(self, root, max_sum):
        if not root:
            return 0
        la = self.max_sum_path_utility(root.left, max_sum)
        ra = self.max_sum_path_utility(root.right, max_sum)
        big_edge = max(la + root.key, ra + root.key)
        max_sum[0] = max(max_sum[0],max(la, max(ra, big_edge)))
        max_sum[0] = max(max_sum[0], la + ra + root.key)
        return big_edge

    def max_sum_path(self, root):
        max_sum = [-1]
        self.max_sum_path_utility(root, max_sum)
        return max_sum[0]

    def largest_sum_subtree_utility(self, root, max_sum):
        if not root:
            return 0
        ls = self.largest_sum_subtree_utility(root.left,max_sum)
        rs = self.largest_sum_subtree_utility(root.right,max_sum)
        max_sum[0] = max(max(max_sum[0],ls),rs)
        max_sum[0] = max(max_sum[0],ls+rs+root.key)
        return ls + rs + root.key

    def largest_sum_subtree(self, root):
        max_sum = [-1]
        self.largest_sum_subtree_utility(root, max_sum)
        return max_sum[0]

    # prints downward paths only
    def print_k_path_sum(self, root, path, k):

        if not root:
            return
        path.append(root.key)
        self.print_k_path_sum(root.left, path=copy.deepcopy(path), k=k)
        self.print_k_path_sum(root.right, path=copy.deepcopy(path), k=k)

        # now we have path till this node.
        sum = 0
        for i in range(len(path)-1 , -1,-1):
            sum += path[i]
            # print sum,
            if sum == k:
                # print 'YIKES !!!\n' , path , '\n'
                print path[i:len(path)] , '\n'
                # for each in pr_path:
                    # print each ,
                # print '\n'

    def subtree_with_given_sum_utilty(self, root,flag, sum):
        if not root:
            return 0
        ls = self.subtree_with_given_sum_utilty(root.left, flag=flag, sum=sum)
        rs = self.subtree_with_given_sum_utilty(root.right, flag = flag, sum=sum)

        # print ls , rs , root.key , '\n'
        if ls + rs + root.key == sum:
            flag[0] = True
        return ls + rs + root.key

    def subtree_with_given_sum(self, root, sum):
        flag = [False]
        self.subtree_with_given_sum_utilty(root, flag, sum)
        if flag[0]:
            return "YES"
        else:
            return "NO"


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
    # n1 = TreeNode(-15)
    # n2 = TreeNode(5)
    # n3 = TreeNode(6)
    # n4 = TreeNode(-8)
    # n5 = TreeNode(1)
    # n6 = TreeNode(3)
    # n7 = TreeNode(9)
    # n8 = TreeNode(2)
    # n9 = TreeNode(6)
    # n10 = TreeNode(0)
    # n11 = TreeNode(4)
    # n12 = TreeNode(-1)
    # n13 = TreeNode(10)
    # n1.left = n2
    # n1.right = n3
    # n2.left = n4
    # n2.right = n5
    # n3.left = n6
    # n3.right = n7
    # n4.left = n8
    # n4.right = n9
    # n7.right = n10
    # n10.left = n11
    # n10.right = n12
    # n12.left = n13


    tree = BinaryTree(root=n1)  # n1 as a root
    # print tree.max_sum_path(tree.root)
    # path = []
    # tree.print_k_path_sum(root=tree.root,path=path,k=16)
    # l = [0]
    # tree.check(l, root=tree.root , count=1)
    # print 'Final ' , l
    print tree.subtree_with_given_sum(root=tree.root,sum=220)