class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        current_level = 0
        current_vertical = 0
        result = list()
        queue = [(root, current_vertical , current_level)] # node, vertical, level 

        while queue:
            length_of_nodes_at_current_level = len(queue)

            for i in range(length_of_nodes_at_current_level):
                node, current_vertical, current_level = queue.pop(0)
                result.append((node.val, current_vertical, current_level))
                if node.left:
                    queue.append((node.left, current_vertical-1, current_level+1))
                if node.right:
                    queue.append((node.right, current_vertical+1, current_level+1))
        
        return result
                
