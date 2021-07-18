# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# import pdb;
class Solution:    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def symmetric(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and \
                   symmetric(p.left, q.right) and symmetric(p.right, q.left)
        
        return symmetric(root.left, root.right)

# if __name__ == '__main__':
#     solution = Solution()
#     testTree = 
#     print(solution.isSymmetric())