def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        '''
        Recursive sol (harder)
        '''
        
        
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        
        
        '''
        Iterative sol (easier)
        '''
        
#         stack = [root]
#         while stack:
#             cur = stack.pop()
#             print(cur.val)
#             if cur.left is None and cur.right is None:
#                 if cur.val == targetSum:
#                     return True
#             if cur.left is not None:
#                 cur.left.val += cur.val
#                 sub = cur.left
#                 stack.append(sub)
#             if cur.right is not None:
#                 cur.right.val += cur.val
#                 cur = cur.right
#                 stack.append(cur)
                
        
#         return False