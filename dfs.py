graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

def dfs(vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor, visited)

visited = set()
dfs(0, visited)


# Non-recursive (iterative) DFS added below — uses an explicit stack and returns the traversal order
def dfs_iterative(start):
    visited = set()
    order = []
    stack = [start]

    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        order.append(v)
        # push neighbors in reverse so we visit them in the same order as the recursive version
        for nbr in reversed(graph.get(v, [])):
            if nbr not in visited:
                stack.append(nbr)

    return order


print()  # newline to separate outputs
print("Iterative:", end=' ')
order = dfs_iterative(0)
for x in order:
    print(x, end=' ')

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS - DFS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is Depth-First Search (DFS)?
A1: Graph traversal algorithm that explores as far as possible along each branch before backtracking
    - Goes deep into graph before exploring breadth
    - Uses stack (LIFO) data structure - either explicit stack or recursion call stack
    - Two implementations: recursive (natural) and iterative (explicit stack)

Q2: What data structure does DFS use and why?
A2: Stack (Last In, First Out - LIFO)
    - Recursive DFS: uses function call stack implicitly
    - Iterative DFS: uses explicit stack data structure
    - LIFO order ensures depth-first exploration pattern

Q3: What is the time complexity of DFS?
A3: O(V + E) where V = vertices, E = edges
    - Each vertex visited exactly once: O(V)
    - Each edge examined exactly once: O(E)
    - Same as BFS - both are optimal for graph traversal

Q4: What is the space complexity of DFS?
A4: O(V) in worst case, O(h) average case where h = height
    - Recursive: call stack depth = O(h), can be O(V) for linear graphs
    - Iterative: explicit stack size = O(V) worst case
    - Generally better than BFS for sparse, deep graphs

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q5: Compare recursive vs iterative DFS implementation?
A5: 
    Recursive DFS:
    ✓ More intuitive and easier to code
    ✓ Natural representation of backtracking
    ✗ Stack overflow risk for deep graphs
    ✗ Less control over traversal order
    
    Iterative DFS:
    ✓ No recursion depth limits
    ✓ More control over traversal order
    ✓ Can be paused/resumed easily
    ✗ More complex code with explicit stack management

Q6: Why might DFS and BFS produce different traversal orders?
A6: Different exploration strategies:
    - DFS: explores first neighbor completely before second neighbor
    - BFS: explores all immediate neighbors before their neighbors
    - Same graph can have multiple valid DFS/BFS orders depending on:
      * Order of neighbors in adjacency list
      * Starting vertex choice
      * Implementation details

Q7: How does DFS detect cycles in a graph?
A7: Track node states during traversal:
    - WHITE: unvisited
    - GRAY: currently being processed (in recursion stack)
    - BLACK: completely processed
    - Cycle detected if we encounter GRAY node (back edge)
    
Q8: What are the different types of edges in DFS tree?
A8: Four types of edges in directed graphs:
    - Tree edges: edges in DFS tree (parent to child)
    - Back edges: from descendant to ancestor (indicate cycles)
    - Forward edges: from ancestor to descendant (not in tree)
    - Cross edges: between nodes in different subtrees

🎯 ADVANCED LEVEL QUESTIONS:

Q9: How to use DFS for topological sorting?
A9: DFS-based topological sort algorithm:
    1. Perform DFS on entire graph
    2. When finishing a vertex (all neighbors processed), add to result list
    3. Reverse the result list for topological order
    4. Works only for DAGs (Directed Acyclic Graphs)
    
    ```python
    def topological_sort_dfs(graph):
        visited = set()
        result = []
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            result.append(node)  # Add after processing all neighbors
        
        for node in graph:
            if node not in visited:
                dfs(node)
        
        return result[::-1]  # Reverse for correct order
    ```

Q10: Implement DFS to find all paths between two nodes?
A10: Modify DFS to track and collect all possible paths:
     ```python
     def find_all_paths_dfs(graph, start, end, path=[]):
         path = path + [start]
         if start == end:
             return [path]
         
         paths = []
         for neighbor in graph[start]:
             if neighbor not in path:  # Avoid cycles
                 new_paths = find_all_paths_dfs(graph, neighbor, end, path)
                 paths.extend(new_paths)
         return paths
     ```

Q11: How to use DFS for strongly connected components?
A11: Kosaraju's algorithm using two DFS passes:
     1. Perform DFS on original graph, record finish times
     2. Create transpose graph (reverse all edges)
     3. Perform DFS on transpose in decreasing finish time order
     4. Each DFS tree in second pass is one SCC

Q12: What is the difference between pre-order and post-order DFS?
A12: 
     Pre-order DFS: Process node before visiting children
     - Visit node → Process node → Visit children
     - Natural for tree traversals, expression evaluation
     
     Post-order DFS: Process node after visiting children  
     - Visit node → Visit children → Process node
     - Useful for dependency resolution, calculating subtree properties

🎯 IMPLEMENTATION QUESTIONS:

Q13: How to modify DFS to find shortest path?
A13: Standard DFS doesn't guarantee shortest path:
     - DFS finds any path, not necessarily shortest
     - For shortest path in unweighted graphs: use BFS
     - For weighted graphs: use Dijkstra's or Bellman-Ford
     - Can modify DFS to find shortest by exploring all paths (inefficient)

Q14: Implement DFS with path tracking?
A14: Track current path during traversal:
     ```python
     def dfs_with_path(graph, start, target, visited=None, path=None):
         if visited is None:
             visited = set()
         if path is None:
             path = []
         
         visited.add(start)
         path.append(start)
         
         if start == target:
             return path.copy()
         
         for neighbor in graph[start]:
             if neighbor not in visited:
                 result = dfs_with_path(graph, neighbor, target, visited, path)
                 if result:
                     return result
         
         path.pop()  # Backtrack
         return None
     ```

Q15: How to implement DFS for maze solving?
A15: Treat maze as graph and use DFS with backtracking:
     ```python
     def solve_maze_dfs(maze, start, end):
         rows, cols = len(maze), len(maze[0])
         visited = set()
         
         def dfs(r, c, path):
             if (r, c) == end:
                 return path + [(r, c)]
             
             visited.add((r, c))
             
             # Try all 4 directions
             for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                 nr, nc = r + dr, c + dc
                 if (0 <= nr < rows and 0 <= nc < cols and 
                     maze[nr][nc] != 1 and (nr, nc) not in visited):
                     result = dfs(nr, nc, path + [(r, c)])
                     if result:
                         return result
             
             visited.remove((r, c))  # Backtrack
             return None
         
         return dfs(start[0], start[1], [])
     ```

Q16: How to use DFS for detecting bipartite graphs?
A16: Use DFS with 2-coloring approach:
     ```python
     def is_bipartite_dfs(graph):
         color = {}
         
         def dfs(node, c):
             color[node] = c
             for neighbor in graph[node]:
                 if neighbor in color:
                     if color[neighbor] == c:
                         return False  # Same color - not bipartite
                 else:
                     if not dfs(neighbor, 1 - c):
                         return False
             return True
         
         for node in graph:
             if node not in color:
                 if not dfs(node, 0):
                     return False
         return True
     ```

Q17: Implement DFS for tree serialization/deserialization?
A17: Use pre-order DFS for tree serialization:
     ```python
     def serialize_tree_dfs(root):
         def dfs(node):
             if not node:
                 return "null,"
             return str(node.val) + "," + dfs(node.left) + dfs(node.right)
         return dfs(root)
     
     def deserialize_tree_dfs(data):
         def dfs():
             val = next(vals)
             if val == "null":
                 return None
             node = TreeNode(int(val))
             node.left = dfs()
             node.right = dfs()
             return node
         
         vals = iter(data.split(","))
         return dfs()
     ```

Q18: How to count connected components using DFS?
A18: Run DFS from each unvisited node:
     ```python
     def count_components_dfs(graph):
         visited = set()
         count = 0
         
         def dfs(node):
             visited.add(node)
             for neighbor in graph[node]:
                 if neighbor not in visited:
                     dfs(neighbor)
         
         for node in graph:
             if node not in visited:
                 dfs(node)
                 count += 1
         
         return count
     ```
"""

# ------------------------
# Commented duplicate: line-by-line explanation of the code above
# The block below is a copy of the script with each original code line commented out
# and preceded by one or more comment lines that explain what that line does.
# Keep this block commented so it has no runtime effect; it's for learning/documentation.
# ------------------------

# Explanation: `graph` is an adjacency list represented as a Python dictionary.
# Keys are node identifiers and values are lists of neighbor node identifiers.
# This representation is efficient for sparse graphs and easy to iterate neighbors.
#graph = {
#    0: [1, 2],
#    1: [0, 3, 4],
#    2: [0, 5, 6],
#    3: [1],
#    4: [1],
#    5: [2],
#    6: [2]
#}

# Explanation: define a recursive DFS function named `dfs` that takes a vertex
# and a `visited` set. The `visited` set tracks which nodes have been seen
# to avoid infinite loops on cycles and to ensure each node is processed once.
#def dfs(vertex, visited):
#    # Mark this vertex as visited by adding it into the `visited` set.
#    visited.add(vertex)
#    # Print the current vertex followed by a space instead of a newline.
#    print(vertex, end=' ')
#    # Iterate over each neighbor of the current vertex from the adjacency list.
#    for neighbor in graph[vertex]:
#        # If the neighbor has not been visited, recursively call dfs on it.
#        if neighbor not in visited:
#            dfs(neighbor, visited)

# Explanation: create an empty set to hold visited nodes, then start the
# recursive DFS traversal at node 0 by calling `dfs(0, visited)`.
#visited = set()
#dfs(0, visited)


# Explanation: Non-recursive (iterative) DFS function using an explicit stack.
# It accepts a `start` node, and returns the `order` list with the traversal order.
#def dfs_iterative(start):
#    # `visited` set prevents revisiting nodes.
#    visited = set()
#    # `order` collects the sequence of visited nodes (the traversal result).
#    order = []
#    # `stack` is a LIFO structure used to control which node to visit next.
#    stack = [start]
#
#    # Continue until there are no nodes left on the stack.
#    while stack:
#        # Pop the top node from the stack to process it.
#        v = stack.pop()
#        # If we've already visited it, skip further processing.
#        if v in visited:
#            continue
#        # Mark the popped node as visited.
#        visited.add(v)
#        # Append the node to the traversal order.
#        order.append(v)
#        # Push neighbors onto the stack. Use reversed() so that the left-most
#        # neighbor (first in the adjacency list) is processed before later ones,
#        # matching typical recursive DFS ordering.
#        for nbr in reversed(graph.get(v, [])):
#            if nbr not in visited:
#                stack.append(nbr)
#
#    # Return the traversal order once done.
#    return order


# Explanation: print a blank line to separate outputs and print the label
# for the iterative output. Then call `dfs_iterative(0)` and print its result.
#print()  # newline to separate outputs
#print("Iterative:", end=' ')
#order = dfs_iterative(0)
#for x in order:
#    print(x, end=' ')
