# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def boundary(self, root):
        self.result = [root.data]
        def is_leaf(root):
            return not root.left and not root.right
                
        def left_boundary(root):
            current = root.left
            while current:
                if not is_leaf(current):
                    self.result.append(current.data)
                if current.left:
                    current = current.left
                else:
                    current = current.right
                
        def in_order_traversal(root):
            if is_leaf(root):
                self.result.append(root.data)
                return
            if root.left:
                in_order_traversal(root.left)
            if root.right:
                in_order_traversal(root.right)
        
        def right_boundary(root):
            stack = []
            current = root.right
            while current:
                if not is_leaf(current):
                    stack.append(current.data)
                if current.right:
                    current = current.right
                else:
                    current = current.left
            self.result.extend(reversed(stack))
            
        left_boundary(root)
        in_order_traversal(root)
        right_boundary(root)
        return self.result
        


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()

# Get the boundary traversal
result = solution.boundary(root)

# Print the result
print("Boundary Traversal:", end=" ")
print(result)

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def boundary(self, root):
        self.result = [root.data]
        def is_leaf(root):
            return not root.left and not root.right
                
        def left_boundary(root):
            current = root.left
            while current:
                if not is_leaf(current):
                    self.result.append(current.data)
                if current.left:
                    current = current.left
                else:
                    current = current.right
                
        def in_order_traversal(root):
            if is_leaf(root):
                self.result.append(root.data)
                return
            if root.left:
                in_order_traversal(root.left)
            if root.right:
                in_order_traversal(root.right)
        
        def right_boundary(root):
            stack = []
            current = root.right
            while current:
                if not is_leaf(current):
                    stack.append(current.data)
                if current.right:
                    current = current.right
                else:
                    current = current.left
            self.result.extend(reversed(stack))
            
        left_boundary(root)
        in_order_traversal(root)
        right_boundary(root)
        return self.result
        


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()

# Get the boundary traversal
result = solution.boundary(root)

# Print the result
print("Boundary Traversal:", end=" ")
print(result)

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def boundary(self, root):
        self.result = [root.data]
        def is_leaf(root):
            return not root.left and not root.right
                
        def left_boundary(root):
            current = root.left
            while current:
                if not is_leaf(current):
                    self.result.append(current.data)
                if current.left:
                    current = current.left
                else:
                    current = current.right
                
        def in_order_traversal(root):
            if is_leaf(root):
                self.result.append(root.data)
                return
            if root.left:
                in_order_traversal(root.left)
            if root.right:
                in_order_traversal(root.right)
        
        def right_boundary(root):
            stack = []
            current = root.right
            while current:
                if not is_leaf(current):
                    stack.append(current.data)
                if current.right:
                    current = current.right
                else:
                    current = current.left
            self.result.extend(reversed(stack))
            
        left_boundary(root)
        in_order_traversal(root)
        right_boundary(root)
        return self.result
        


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()

# Get the boundary traversal
result = solution.boundary(root)

# Print the result
print("Boundary Traversal:", end=" ")
print(result)

