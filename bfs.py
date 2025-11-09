# Most basic BFS implementation - iterative with a queue

# Graph represented as adjacency list - each node maps to its neighbors
graph = {
    0: [1, 2],      # Node 0 connects to nodes 1 and 2
    1: [0, 3, 4],   # Node 1 connects to nodes 0, 3, and 4
    2: [0, 5, 6],   # Node 2 connects to nodes 0, 5, and 6
    3: [1, 5],      # Node 3 connects to nodes 1 and 5
    4: [1],         # Node 4 connects only to node 1 
    5: [2],         # Node 5 connects only to node 2
    6: [2]          # Node 6 connects only to node 2
}

def bfs(start):
    """Breadth-First Search traversal starting from given node"""
    visited = set()    # Track visited nodes to avoid cycles
    queue = [start]    # Initialize queue with starting node
    
    while queue:
        # Remove first node from queue (FIFO - First In, First Out)
        node = queue.pop(0)
        
        if node not in visited:
            # Mark node as visited and process it
            visited.add(node)
            print(node, end=' ')
            
            # Add all unvisited neighbors to queue for future exploration
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

print("BFS Traversal starting from node 0:")
bfs(0)


# ========================================================================================
# COMMENTED EXPLANATION - Line-by-line breakdown of the BFS code above
# ========================================================================================

# Explanation: This is an adjacency list representation of a graph.
# Each key is a node (0-6) and the value is a list of its neighbors (connected nodes).
# For example, node 0 is connected to nodes 1 and 2.
# This structure makes it easy to look up all neighbors of any node.
#graph = {
#    0: [1, 2],
#    1: [0, 3, 4],
#    2: [0, 5, 6],
#    3: [1, 5],
#    4: [1],
#    5: [2],
#    6: [2]
#}

# Explanation: Define a BFS function that takes a starting node.
# BFS explores nodes level by level (breadth-first).
#def bfs(start):
#    # Create an empty set to track which nodes we've already visited.
#    # Sets provide O(1) lookup time to check if a node is visited.
#    visited = set()
#    
#    # Initialize a queue with the start node.
#    # A queue is a FIFO (First In First Out) data structure.
#    # We use a Python list here and pop(0) removes from the front.
#    queue = [start]
#    
#    # Keep processing nodes as long as the queue is not empty.
#    while queue:
#        # Remove and get the first node from the queue (FIFO).
#        # pop(0) removes from index 0 (the front of the list).
#        node = queue.pop(0)
#        
#        # Check if we've already visited this node.
#        # This prevents processing the same node multiple times.
#        if node not in visited:
#            # Mark this node as visited by adding it to the set.
#            visited.add(node)
#            
#            # Print the current node followed by a space (no newline).
#            # This shows the order in which nodes are visited.
#            print(node, end=' ')
#            
#            # Look at all neighbors of the current node.
#            # graph[node] returns the list of neighbors for this node.
#            for neighbor in graph[node]:
#                # Only add unvisited neighbors to the queue.
#                # This ensures we don't revisit nodes and avoids infinite loops.
#                if neighbor not in visited:
#                    # Add the neighbor to the end of the queue.
#                    # It will be processed later (FIFO order).
#                    queue.append(neighbor)

# Explanation: Start the BFS traversal from node 0.
# This call executes the BFS and prints the traversal order.
#bfs(0)


# ========================================================================================
# DFS vs BFS COMPARISON - How they work differently
# ========================================================================================

# DFS (Depth-First Search):
# - Uses a STACK (Last In First Out - LIFO)
# - Goes as DEEP as possible before backtracking
# - Can be implemented recursively (uses call stack) or iteratively (explicit stack)
# - Order: Visit node -> Go deep into first unvisited neighbor -> Backtrack when stuck
# 
# Example DFS traversal from node 0:
#   0 -> 1 -> 3 -> 4 (dead end, backtrack) -> 2 -> 5 -> 6
#   Goes deep first: 0→1→3, then backs up to explore 4, then backs up to explore 2's branch
#
# DFS use cases:
#   - Finding paths between nodes
#   - Detecting cycles
#   - Topological sorting
#   - Solving mazes

# BFS (Breadth-First Search):
# - Uses a QUEUE (First In First Out - FIFO)
# - Explores all neighbors at current LEVEL before moving to next level
# - Always iterative (needs a queue data structure)
# - Order: Visit node -> Visit all its neighbors -> Visit neighbors' neighbors, etc.
#
# Example BFS traversal from node 0:
#   0 -> 1, 2 (level 1) -> 3, 4, 5, 6 (level 2)
#   Goes wide first: explores level by level
#
# BFS use cases:
#   - Finding shortest path (unweighted graph)
#   - Level-order traversal
#   - Finding all nodes within k distance
#   - Social network connections (friends of friends)

# Key Difference Summary:
# ┌─────────────┬────────────────────┬──────────────────────┐
# │   Feature   │        DFS         │         BFS          │
# ├─────────────┼────────────────────┼──────────────────────┤
# │ Data Struct │ Stack (LIFO)       │ Queue (FIFO)         │
# │ Exploration │ Go deep first      │ Go wide (level)      │
# │ Memory      │ O(height)          │ O(width)             │
# │ Shortest    │ No guarantee       │ Yes (unweighted)     │
# │ Implementation│ Recursive/Iterative│ Iterative only      │
# └─────────────┴────────────────────┴──────────────────────┘

# Visual Example for graph starting at 0:
#       0
#      / \
#     1   2
#    /|   |\
#   3 4   5 6
#
# DFS order: 0 → 1 → 3 → 4 → 2 → 5 → 6  (goes deep left first)
# BFS order: 0 → 1 → 2 → 3 → 4 → 5 → 6  (level by level: 0, then 1&2, then 3&4&5&6)

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS - BFS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is Breadth-First Search (BFS)?
A1: Graph traversal algorithm that explores nodes level by level
    - Visits all nodes at distance k before visiting nodes at distance k+1
    - Uses queue (FIFO) data structure for implementation
    - Guarantees shortest path in unweighted graphs

Q2: What data structure does BFS use and why?
A2: Queue (First In, First Out - FIFO)
    - Ensures nodes are processed in order of discovery
    - Maintains level-by-level exploration pattern
    - Contrast with DFS which uses stack (LIFO)

Q3: What is the time complexity of BFS?
A3: O(V + E) where V = vertices, E = edges
    - Each vertex visited exactly once: O(V)
    - Each edge examined exactly once: O(E)
    - Total: O(V + E) - optimal for graph traversal

Q4: What is the space complexity of BFS?
A4: O(V) in worst case
    - Queue can hold at most all vertices at one level
    - Visited set stores all vertices: O(V)
    - In complete binary tree: queue holds O(V/2) nodes at last level

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q5: Why does BFS find shortest path in unweighted graphs?
A5: Level-by-level exploration guarantees optimality:
    - First time a node is reached, it's via shortest path
    - Any longer path would be discovered later (higher level)
    - Greedy property: local optimum (first discovery) equals global optimum

Q6: How to modify BFS to find shortest path distance?
A6: Track distance/level information:
    - Use queue of (node, distance) pairs
    - Or maintain separate distance array
    - Distance[neighbor] = distance[current] + 1

Q7: What's the difference between BFS tree and original graph?
A7: BFS tree is spanning tree of original graph:
    - Contains all vertices from original graph
    - Has exactly V-1 edges (tree property)
    - Edges represent parent-child relationships in BFS traversal
    - Multiple BFS trees possible for same graph

Q8: How does BFS handle disconnected graphs?
A8: BFS explores only one connected component:
    - Visits all nodes reachable from starting node
    - Unreachable nodes remain unvisited
    - To visit all nodes: run BFS from multiple starting points

🎯 ADVANCED LEVEL QUESTIONS:

Q9: Compare BFS vs DFS for different applications?
A9: 
    BFS advantages:
    - Shortest path in unweighted graphs
    - Level-order traversal
    - Finding nodes within k distance
    - Better for wide, shallow graphs
    
    DFS advantages:
    - Path finding (any path, not necessarily shortest)
    - Topological sorting
    - Cycle detection
    - Better for narrow, deep graphs
    - Lower space complexity for sparse graphs

Q10: How to implement bidirectional BFS?
A10: Run BFS from both source and target simultaneously:
     - Maintain two queues and visited sets
     - Alternate between forward and backward search
     - Stop when searches meet (intersection of visited sets)
     - Reconstruct path by combining both directions
     - Can be much faster for long paths

Q11: What is multi-source BFS?
A11: BFS starting from multiple source nodes simultaneously:
     - Initialize queue with all source nodes
     - Useful for finding shortest distance from any source
     - Applications: nearest facility problem, wildfire spread simulation
     - All sources treated as being at distance 0

Q12: How to use BFS for bipartite graph checking?
A12: Use BFS with 2-coloring:
     - Color starting node with color 0
     - Color each neighbor with opposite color
     - If neighbor already has same color: not bipartite
     - If BFS completes without conflicts: bipartite

🎯 IMPLEMENTATION QUESTIONS:

Q13: Implement BFS that returns the actual shortest path?
A13: Track parent pointers during traversal:
     ```python
     def bfs_path(graph, start, end):
         queue = [start]
         visited = {start}
         parent = {start: None}
         
         while queue:
             node = queue.pop(0)
             if node == end:
                 # Reconstruct path
                 path = []
                 while node:
                     path.append(node)
                     node = parent[node]
                 return path[::-1]
             
             for neighbor in graph[node]:
                 if neighbor not in visited:
                     visited.add(neighbor)
                     parent[neighbor] = node
                     queue.append(neighbor)
         return None
     ```

Q14: How to implement BFS iteratively vs recursively?
A14: BFS is naturally iterative due to queue requirement:
     - Iterative: explicit queue management (standard approach)
     - Recursive: possible but requires passing queue between calls
     - Iterative is preferred: clearer logic, no recursion depth limits

Q15: Optimize BFS for dense vs sparse graphs?
A15: Different optimizations based on graph density:
     
     Sparse graphs (few edges):
     - Adjacency list representation
     - Check if neighbor in visited set before adding to queue
     
     Dense graphs (many edges):
     - Adjacency matrix for O(1) edge lookup
     - Bit vectors for visited tracking
     - Consider using array instead of set for visited

Q16: How to handle weighted graphs with BFS?
A16: Standard BFS doesn't work optimally with weighted graphs:
     - BFS finds shortest path by number of edges, not by weight
     - For weighted graphs, use Dijkstra's algorithm
     - Exception: if all weights are equal, BFS still works

Q17: Implement BFS for tree vs graph structures?
A17: 
     Tree BFS (simpler - no cycle checking needed):
     ```python
     def bfs_tree(root):
         if not root:
             return
         queue = [root]
         while queue:
             node = queue.pop(0)
             print(node.val)
             if node.left:
                 queue.append(node.left)
             if node.right:
                 queue.append(node.right)
     ```
     
     Graph BFS (needs visited tracking):
     - Must maintain visited set to avoid cycles
     - More complex but handles arbitrary graph structures

Q18: How to find all nodes at exactly distance k using BFS?
A18: Track level/distance during BFS:
     ```python
     def nodes_at_distance_k(graph, start, k):
         queue = [(start, 0)]  # (node, distance)
         visited = {start}
         result = []
         
         while queue:
             node, dist = queue.pop(0)
             if dist == k:
                 result.append(node)
             elif dist < k:
                 for neighbor in graph[node]:
                     if neighbor not in visited:
                         visited.add(neighbor)
                         queue.append((neighbor, dist + 1))
         return result
     ```
"""
