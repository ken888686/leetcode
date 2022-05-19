from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left = right = 1
        if root.left != None:
            left += self.maxDepth(root.left)
        if root.right != None:
            right += self.maxDepth(root.right)

        return max(left, right)


sol = Solution()
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), None))
print(sol.maxDepth(tree))
