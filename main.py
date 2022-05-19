from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []
        while stack or root:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                root = temp.right
        return result


sol = Solution()
tree = TreeNode(1, None, TreeNode(2, TreeNode(
    3, TreeNode(5), TreeNode(6)), TreeNode(4)))
print(sol.inorderTraversal(tree))
