from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def isSymmetricByWhileLoop(self, root: Optional[TreeNode]) -> bool:
        stack: List[TreeNode] = []
        stack.append(root.right)
        stack.append(root.left)
        while len(stack) > 0:
            t1 = stack.pop()
            t2 = stack.pop()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None or t1.val != t2.val:
                return False
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)
        return True

    def isSymmetricByRecursive(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 == None and tree2 == None:
            return True
        if tree1 == None or tree2 == None or tree1.val != tree2.val:
            return False
        return self.checkSymmetric(tree1.left, tree2.right) and self.checkSymmetric(tree1.right, tree2.left)


sol = Solution()
myTree = TreeNode(1,
                  TreeNode(2, TreeNode(3), None),
                  TreeNode(2, None, TreeNode(3)))
# print(sol.isSymmetricByWhileLoop(myTree))
print(sol.isSymmetricByRecursive(myTree))
print(sol.isSymmetricByRecursive())
