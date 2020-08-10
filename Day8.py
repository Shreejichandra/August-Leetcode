#PATH SUM III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        # approach: examine sum for both subtrees and remember to run 
        #           children even if there is a valid path found

        if not root:
            return 0
        return self.pathSumRecursive(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumRecursive(self, root, sum):
        if not root:
            return 0

        return (1 if root.val == sum else 0) + self.pathSumRecursive(root.left, sum - root.val) + self.pathSumRecursive(root.right, sum - root.val)
        
