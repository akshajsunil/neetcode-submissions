from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to map original nodes to their cloned counterparts
        # Map: {original_node: cloned_node}
        visited = {}
        
        # Initialize the first cloned node and put it in the map
        visited[node] = Node(node.val)
        
        q = deque([node])
        
        while q:
            n = q.popleft()
            
            # Iterate through all neighbors of the current original node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # If neighbor hasn't been cloned yet, clone it and add to map
                    visited[neighbor] = Node(neighbor.val)
                    # Add the original neighbor to the queue for future processing
                    q.append(neighbor)
                
                # Retrieve the cloned current node, and append the cloned neighbor to it.
                # This happens whether the neighbor was just created or created previously,
                # ensuring all bidirectional edges are connected.
                visited[n].neighbors.append(visited[neighbor])
                
        # Return the clone of the starting node
        return visited[node]