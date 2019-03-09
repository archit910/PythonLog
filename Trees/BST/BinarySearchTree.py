import copy

class TreeNode:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key


class BSTree:

    def __init__(self , root):
        self.root = root

    def pre_order(self, root):
        if not root:
            return
        print root.key ,
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)

        print root.key ,

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print root.key,
        self.inorder(root.right)

    def insert(self, root, key):
        if not root:
            # insert here
            new_node = TreeNode(key)
            if not self.root:
                self.root = new_node
            return new_node
        if root.key < key:
            root.right = self.insert(root.right , key)
        else:
            root.left = self.insert(root.left , key)

    def get_lca(self, root, key1, key2):

        #Pre order traversal
        if not root:
            return None
        if root.key >= key1 and root.key <= key2:
            return root

        l_lca = self.get_lca(root.left, key1, key2)
        r_lca = self.get_lca(root.right , key1, key2)
        return l_lca or r_lca

    def ceil_value(self, root, k):

        if not root:
            return -1
        if k == root.key:
            return root.key
        if k > root.key:
            return self.ceil_value(root.right, k)
        la = self.ceil_value(root.left, k)
        val = la if la >=k else root.key
        return val

if __name__ == '__main__':
    bst = BSTree(None) #Empty Tree
    bst.insert(bst.root , 4)
    bst.insert(bst.root, 1)
    bst.insert(bst.root, 6)
    # bst.inorder(bst.root)
    # print bst.get_lca(bst.root, 1 , 7).key
    print bst.ceil_value(bst.root, 5)



