class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_setup():
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(15)

    left_left = TreeNode(3)
    left_right = TreeNode(7)

    right_right = TreeNode(18)

    left.left = left_left
    left.right = left_right

    right.right = right_right

    root.left = left
    root.right = right

    return root


def inorder_traverse(root, low, high):
    result = 0
    if root.left:
        result += inorder_traverse(root.left, low, high)

    if root.val >= low and root.val <= high:
        result += root.val

    if root.right:
        result += inorder_traverse(root.right, low, high)

    return result

if __name__ == '__main__':
    root = example_setup()
    assert 32 == inorder_traverse(root, 7, 15)
