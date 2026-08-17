class TreeNode:
    def __init__(self, value=None, right=None, left=None):
        self.val = value
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)


class BinaryTree:
    def __init__(self, root: TreeNode = None):
        self.root = root

    def add(self, value):
        if not self.root:
            self.root = value
        else:
            cur = self.root
            while True:
                if value > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = TreeNode(value)
                        break

                elif value < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = TreeNode(value)
                        break
                else:
                    raise ValueError("This value is already in tree")

    def remove(self, value):
        if not self.has_value(value):
            raise ValueError("Value not in tree")

        cur = self.root
        parent = None

        while cur.left or cur.right:
            if value > cur.val:
                parent = cur
                cur = cur.right
            elif value < cur.val:
                parent = cur
                cur = cur.left
            elif value == cur.val:
                break

        if cur.left and cur.right:
            change = cur.left
            change_parent = cur

            while change.right:
                change_parent = change
                change = change.rightc

            cur.val = change.val

            if change_parent == cur:
                change_parent.left = change.left
            else:
                change_parent.right = change.left

        elif cur.left and not cur.right:
            if parent is None:
                self.root = cur.left
            elif parent.left == cur:
                parent.left = cur.left
            else:
                parent.right = cur.left

        elif not cur.left and cur.right:
            if parent is None:
                self.root = cur.right
            elif parent.right == cur:
                parent.right = cur.right
            else:
                parent.left = cur.right
        
        elif not cur.left and not cur.right:
            if parent is None:
                self.root = None
            elif parent.left == cur:
                parent.left = None
            else:
                parent.right = None

    def get_max(self):
        cur = self.root

        while cur.right:
            cur = cur.right

        return cur.val

    def get_min(self):
            cur = self.root
    
            while cur.left:
                cur = cur.left
    
            return cur.val

    def has_value(self, value):
        cur = self.root

        while cur:
            if value > cur.val:
                cur = cur.right
            elif value < cur.val:
                cur = cur.left
            elif value == cur.val:
                return True

        if cur.val == value:
            return True

        return False

    def __str__(self):
        tree = []

        def whole_tree(node):
            if node is None:
                return

            whole_tree(node.left)
            tree.append(node.val)
            whole_tree(node.right)

        whole_tree(self.root)

        return str(tree)