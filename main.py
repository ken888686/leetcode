from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                root = tmpNode.right
        return ans


sol = Solution()
tree = TreeNode(1, None, TreeNode(2, TreeNode(
    3, TreeNode(5), TreeNode(6)), TreeNode(4)))
print(sol.inorderTraversal(tree))
