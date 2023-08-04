class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

# The logic behind the code is as follows:

# We start with an empty result list and an empty stack to store nodes.
# We initialize the current variable with the root of the binary tree.
# We use a while loop to traverse the tree until either the current node becomes None (indicating that we have visited all nodes) or the stack becomes empty but there are still nodes in the tree that need to be visited.
# Inside the while loop, we traverse to the leftmost node by repeatedly pushing the left child of the current node onto the stack until we reach a node with no left child.
# After reaching the leftmost node, we pop it from the stack, visit it (add its value to the result list), and then move to its right subtree by setting current to its right child.
# The process continues as we traverse the tree in an in-order manner, visiting left subtree first, then the current node, and finally the right subtree.
# The in-order traversal is stored in the result list, which is returned after the while loop completes.
# The key insight here is that by using a stack, we can simulate the recursive call stack that is used in a recursive in-order traversal. We traverse to the leftmost node first, then we backtrack to the parent nodes and visit them, and finally, we move to the right subtree of each visited node. This allows us to perform an in-order traversal iteratively.

# The in-order traversal visits nodes in non-decreasing order for a binary search tree (BST). For a general binary tree, it visits nodes in the order left subtree, current node, right subtree, which may not be in sorted order. However, for the example binary tree provided earlier (with values [1, 2, 3, 4, 5, 6, 7]), it will indeed produce the in-order traversal [4, 2, 5, 1, 6, 3, 7] as expected.


def inOrder(root):
    result = []
    stack = []

    current = root
    while current or stack:
        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Pop the leftmost node and visit it
        current = stack.pop()
        result.append(current.data)

        # Move to the right subtree
        current = current.right

    return result


# Example binary tree:     1
#                        /   \
#                       2     3
#                      / \   / \
#                     4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(inOrder(root))  # Output: [4, 2, 5, 1, 6, 3, 7]
