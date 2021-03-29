def isSymmetric(self, root: TreeNode) -> bool:
        
        # create a new function to check for symmetry
#         def isym(root1, root2):
#             # looking for similarity
#             if root1 is None and root2 is None:
#                 return True
#             elif root1 is None and root2 is not None:
#                 return False
#             elif root1 is not None and root2 is None:
#                 return False
#             else:
#                 if root1.val != root2.val:
#                     return False
#                 else:
#                     return isym(root1.left, root2.right) and isym(root1.right, root2.left)
            
            
#         if root == None:
#             return True
#         else:
#             return isym(root.left, root.right)
        if root == None:
            return True
        stack = [root,root]
        while stack:
            r1 = stack.pop()
            r2 = stack.pop()
            
            if r1 is None and r2 is not None:
                return False
            elif r1 is not None and r2 is None:
                return False
            elif r1 is not None and r2 is not None:
                if r1.val != r2.val:
                    return False
            if r1 is not None:
                stack.append(r1.left)
                stack.append(r2.right)
                stack.append(r1.right)
                stack.append(r2.left)
        
        return True