from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return \
            root if root is None or val == root.val else \
            self.searchBST(root.left, val) if val < root.val else \
            self.searchBST(root.right, val) if val > root.val else \
            None

print(Solution().searchBST(TreeNode(val = 4, left=TreeNode(val = 2, left=TreeNode(val = 1), right=TreeNode(val = 3)), right=TreeNode(val = 7)), 2))  # Output: TreeNode(2)