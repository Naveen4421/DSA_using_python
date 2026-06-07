# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        from collections import defaultdict
        nodes = {}
        children = set()

        def get(val):
            if val not in nodes:
                nodes[val] = TreeNode(val)
            return nodes[val]

        for parent, child, is_left in descriptions:
            p_node = get(parent)
            c_node = get(child)
            if is_left:
                p_node.left = c_node
            else:
                p_node.right = c_node
            children.add(child)

        # Root is the only value that was never someone's child
        for val, node in nodes.items():
            if val not in children:
                return node
        
