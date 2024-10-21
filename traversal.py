class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key: # is 30 < 50
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def in_order_traversal(self):
        self._in_order_traversal_recursive(self.root)
        print()
    
    def _in_order_traversal_recursive(self, node):
        if node:
            self._in_order_traversal_recursive(node.left)
            print(node.key, end=" ")
            self._in_order_traversal_recursive(node.right)

    def pre_order_traversal(self):
        self._pre_order_traversal_recursive(self.root)
        print()
    
    def _pre_order_traversal_recursive(self, node):
        if node:
            print(node.key, end=" ")
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)

    def post_order_traversal(self):
        self._post_order_traversal_recursive(self.root)
        print()

    def _post_order_traversal_recursive(self, node):
        if node:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.key, end=" ")
    
    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, depth):
        if node is None:
            return
        self._print_tree_recursive(node.right, depth + 1)
        print("    " * depth + str(node.key))
        self._print_tree_recursive(node.left, depth + 1)

if __name__ == "__main__":
    tree = BinaryTree()

    # Insert keys
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        tree.insert(key) 
    
    # In-order traversal
    print("In-order traversal:")
    tree.in_order_traversal()

    # Pre-order traversal
    print("Pre-order traversal:")
    tree.pre_order_traversal()

    # Post-order traversal
    print("Post-order traversal:")
    tree.post_order_traversal()

    print("Binary tree structure:")
    tree.print_tree()





    



    
    
    