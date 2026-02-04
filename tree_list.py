class TreeNode:

    def __init__(self, value, left_des, right_des):
        self.value = value
        self.left_des = left_des
        self.right_des = right_des

class BinaryTree:

    def __init__(self, root):
        self.root = root

    def add(self, value):
        self.add_rec(value, self.root)
    
    def add_rec(self, value, node):
        if node :
            node = TreeNode(value, None, None)
        if value < node.value:
            self.add_rec(value, node.left_des)
    
    def find(self, value):
        return self.find_rec(value, self.root)

    def find_rec(self, value, node):
        if node == None:
            return None
        if value == node.value:
            return node.value
        elif value < node.value:
            return self.find_rec(value, node.left_des)
        else:
            return self.find_rec(value, node.right_des)


myTree = BinaryTree(TreeNode(10, TreeNode(5, None, None), TreeNode(18, None, None)))
print(myTree.find(27))
