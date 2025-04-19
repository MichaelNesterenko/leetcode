from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dpath_calc(depth: int, nodes: List[TreeNode]) -> int:
            next_nodes = [ ]
            has_node = False
            for node in nodes:
                has_node |= node is not None
                if node and node.left:
                    next_nodes.append(node.left)
                if node and node.right:
                    next_nodes.append(node.right)
            return depth + (1 if has_node else 0) if not next_nodes else dpath_calc(depth + 1, next_nodes)
        return dpath_calc(0, [ root ])