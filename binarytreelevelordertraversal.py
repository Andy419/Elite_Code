def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # iterative solution is easier than recursion (bfs)
        stack = [root]
        levels = []
        while stack:
            nstack = stack
            stack = []
            level = []

            # add to new stack left and right of each cur node if it is not None
            while nstack:
                cur = nstack.pop(0)
                if cur is not None:
                    level.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)
            if level != []:
                levels.append(level)
        return levels