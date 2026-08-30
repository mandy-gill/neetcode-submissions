# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(cur):
            if not cur: return False

            if cur.val == subRoot.val and checkSub(cur, subRoot):
                return True
            
            return dfs(cur.left) or dfs(cur.right)

        def checkSub(cur, sub):
            if not cur and not sub:
                return True
            if not cur or not sub or cur.val != sub.val:
                return False
                
            return (checkSub(cur.left, sub.left) and checkSub(cur.right,sub.right))

        return dfs(root)