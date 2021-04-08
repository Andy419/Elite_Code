def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ''' bit tricky and kinda impossible to do without knowing the trick.
            basically you go left and right and if you hit you return
            if you hit left but not right, it means both are left and
            the common one is the first one. vise versa for right
            if left and right exist, then there common is the intial root
        '''
        
        
        if root is None:
            return None
        
        # if a hit, return the root
        if root is p or root is q:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is not None:
            return root
        elif left is None:
            return right
        else:
            return left