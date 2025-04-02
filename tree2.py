from re import search


class Node:
    def __init__(self, left=None, right=None, val= None):
        self.left = left
        self.right = right
        self.val = val

class tree:
    def __init__(self):
        pass
    
    # recursively 
    def max_depth_recursively(self, node):
        if not node: return 0
        left = max_depth_recursively(node.left)
        right = max_depth_recursively(node.rght)

        return max(left, right) + 1
    
    # iteratively
    def max_depth_iteratively(self, node):
        stack = [(node, 0)] 

        depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                ans = max(ans, depth)
                stack.append(node.left, depth+1)
                stack.append(node.right, depth+1)
            return ans 

    def search(self, node, val):
        if not node:
            return None

        if node.val = val:
            return Node
        if node.val > val:
            return search(node.left, val)
        return search(nodel.right, val)

    def delete(self, node, val):
        if not node:
            return None

        if node.val == val:
            node.right = None
            node.left = None
            return node
        if node.val > val:
            return delete







