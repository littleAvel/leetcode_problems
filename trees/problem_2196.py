from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes_map = {}
        children = set()

        for description in descriptions:
            parent_value = description[0]
            child_value = description[1]
            is_left = bool(description[2])

            if parent_value not in nodes_map:
                nodes_map[parent_value] = TreeNode(parent_value)
            if child_value not in nodes_map:
                nodes_map[child_value] = TreeNode(child_value)

            if is_left:
                nodes_map[parent_value].left = nodes_map[child_value]
            else:
                nodes_map[parent_value].right = nodes_map[child_value]

            children.add(child_value)

        for node in nodes_map.values():
            if node.val not in children:
                return node

        return None