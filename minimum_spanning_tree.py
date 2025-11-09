# Minimum Spanning Tree - using Prim's algorithm (simple version)
# Connects all nodes with minimum total edge weight

def prim_mst(graph):
    """
    Minimum Spanning Tree using Prim's Algorithm
    
    ALGORITHM: Greedy approach to build MST by growing tree one vertex at a time
    1. Start with arbitrary vertex
    2. Repeatedly add minimum weight edge connecting tree to non-tree vertex
    3. Continue until all vertices are included
    
    graph: dict where graph[node] = [(neighbor, weight), ...]
    Returns: list of edges in MST as (node1, node2, weight) and total weight
    """
    # Step 1: Initialize with all nodes in the graph
    nodes = list(graph.keys())  # Get all vertices in the graph
    start = nodes[0]            # Start with first vertex (arbitrary choice)
    
    # Step 2: Initialize data structures
    visited = {start}  # Set of vertices already included in MST
    mst = []          # List to store MST edges
    total_weight = 0  # Track total weight of MST
    
    # Step 3: Main algorithm loop - add vertices one by one
    while len(visited) < len(nodes):
        min_edge = None           # Track minimum weight edge found
        min_weight = float('inf') # Initialize to infinity
        
        # Step 4: Find minimum weight edge crossing the cut
        # Cut = partition between visited (in MST) and unvisited vertices
        for node in visited:  # For each vertex already in MST
            for neighbor, weight in graph[node]:  # Check all its edges
                # Only consider edges to unvisited vertices (crossing edges)
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight  # Update minimum weight
                    min_edge = (node, neighbor, weight)  # Store the edge
        
        # Step 5: Add minimum edge to MST (if found)
        if min_edge:
            node1, node2, weight = min_edge  # Unpack edge components
            mst.append(min_edge)            # Add edge to MST
            visited.add(node2)              # Mark destination vertex as visited
            total_weight += weight          # Update total MST weight
    
    return mst, total_weight

# Example weighted undirected graph - adjacency list representation
# Note: For undirected graph, each edge appears in both directions
graph = {
    'A': [('B', 4), ('C', 2)],          # A connects to B(4), C(2)
    'B': [('A', 4), ('C', 1), ('D', 5)], # B connects to A(4), C(1), D(5)
    'C': [('A', 2), ('B', 1), ('D', 8)], # C connects to A(2), B(1), D(8)
    'D': [('B', 5), ('C', 8)]           # D connects to B(5), C(8)
}

print("MINIMUM SPANNING TREE - PRIM'S ALGORITHM")
print("=" * 50)

# Execute Prim's algorithm
mst, total = prim_mst(graph)

print("MST edges found:")
print("-" * 30)
for i, edge in enumerate(mst, 1):
    print(f"{i}. {edge[0]} -- {edge[1]} (weight: {edge[2]})")

print("-" * 30)
print(f"Total MST weight: {total}")
print(f"Number of edges in MST: {len(mst)}")
print(f"Expected edges for {len(graph)} vertices: {len(graph)-1}")

# Verification
if len(mst) == len(graph) - 1:
    print("✓ Correct number of edges for spanning tree")
else:
    print("✗ Incorrect number of edges")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
PRIM'S MST ALGORITHM STEP-BY-STEP:

PROBLEM: Find minimum weight spanning tree that connects all vertices

SPANNING TREE PROPERTIES:
- Connects all n vertices with exactly n-1 edges
- No cycles (tree property)
- Minimum total weight among all possible spanning trees

PRIM'S STRATEGY:
- Grow MST incrementally by adding one vertex at a time
- Always choose minimum weight edge that connects MST to non-MST vertex
- Greedy choice leads to optimal solution

EXAMPLE EXECUTION (using the graph above):

Initial state:
- Start with vertex A
- visited = {A}, MST = [], total_weight = 0

Step 1: From {A}, available edges: (A,B,4), (A,C,2)
        Choose minimum: (A,C,2)
        visited = {A,C}, MST = [(A,C,2)], total_weight = 2

Step 2: From {A,C}, available edges: (A,B,4), (C,B,1), (C,D,8)
        Choose minimum: (C,B,1)  
        visited = {A,C,B}, MST = [(A,C,2), (C,B,1)], total_weight = 3

Step 3: From {A,C,B}, available edges: (A,B,4), (B,D,5), (C,D,8)
        Note: (A,B,4) ignored because B already visited
        Choose minimum: (B,D,5)
        visited = {A,C,B,D}, MST = [(A,C,2), (C,B,1), (B,D,5)], total_weight = 8

All vertices visited - MST complete!

Final MST:
- Edges: A-C(2), C-B(1), B-D(5)
- Total weight: 8
- This is optimal - no other spanning tree has weight < 8

VISUAL REPRESENTATION:
Original Graph:    MST Result:
    A----4----B        A        B
    |         |        |        |
    2         5   =>   2        5
    |         |        |        |
    C----1----         C----1----D
         |
         8
         |
         D
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is a Minimum Spanning Tree (MST)?
A1: A spanning tree of a weighted graph with minimum total edge weight
    - Spanning tree: connects all vertices with exactly n-1 edges, no cycles
    - Minimum: among all possible spanning trees, has smallest total weight
    - Unique if all edge weights are distinct

Q2: What is the greedy strategy in Prim's algorithm?
A2: Always choose the minimum weight edge that connects the current MST to a new vertex
    - Local optimal choice: pick cheapest available edge
    - Global optimum: greedy choices lead to optimal MST
    - Works due to cut property of MSTs

Q3: What is the time complexity of this Prim's implementation?
A3: O(V²) where V is number of vertices
    - Outer loop runs V-1 times (add V-1 edges)
    - Inner loops scan all edges to find minimum: O(E) ≈ O(V²) for dense graphs
    - Total: O(V × V²) = O(V²)

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: What is the "cut property" and how does it justify Prim's algorithm?
A4: Cut property: For any cut of the graph, the minimum weight edge crossing 
    the cut is in some MST
    - Cut = partition of vertices into two sets
    - Prim's cut: vertices in MST vs vertices not in MST
    - Minimum crossing edge is safe to add to MST
    - Proves correctness of greedy choice

Q5: How does Prim's handle ties (edges with equal weight)?
A5: Algorithm works correctly with ties:
    - Any choice among equal-weight edges leads to valid MST
    - Total weight remains optimal regardless of tie-breaking
    - Different executions may produce different MSTs with same total weight

Q6: Why does Prim's algorithm always produce a tree?
A6: By construction, algorithm maintains tree property:
    - Starts with single vertex (trivial tree)
    - Each iteration adds exactly one vertex and one edge
    - Never creates cycles (only adds edges to unvisited vertices)
    - Stops when all vertices included: exactly n-1 edges

🎯 ADVANCED LEVEL QUESTIONS:

Q7: Compare Prim's vs Kruskal's MST algorithms?
A7: 
    Prim's Algorithm:
    ✓ Vertex-centric: grows tree from single vertex
    ✓ Good for dense graphs
    ✓ Simple implementation with adjacency lists
    ✗ Requires connected graph to work properly
    
    Kruskal's Algorithm:
    ✓ Edge-centric: considers all edges globally
    ✓ Good for sparse graphs  
    ✓ Works on disconnected graphs (finds MST forest)
    ✗ Requires Union-Find for efficient cycle detection

Q8: How would you optimize Prim's algorithm for better performance?
A8: Use priority queue (min-heap) instead of linear search:
    ```python
    import heapq
    
    def prim_optimized(graph):
        start = next(iter(graph))
        visited = {start}
        edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
        heapq.heapify(edges)
        mst = []
        
        while edges and len(visited) < len(graph):
            weight, u, v = heapq.heappop(edges)
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for neighbor, w in graph[v]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (w, v, neighbor))
        return mst
    ```
    Time complexity: O(E log V)

Q9: What happens if the graph is disconnected?
A9: Prim's algorithm finds MST of one connected component:
    - Algorithm terminates when no more edges found (min_edge = None)
    - Results in MST for component containing starting vertex
    - Other components remain unconnected
    - Can run Prim's multiple times to get MST forest

Q10: How to verify if result is actually an MST?
A10: Check three properties:
     1. Spanning: exactly n-1 edges, connects all vertices
     2. Tree: no cycles (can verify with DFS/BFS)
     3. Minimum: compare with other spanning trees (complex)
     - If algorithm is correct, first two properties sufficient

🎯 IMPLEMENTATION QUESTIONS:

Q11: How to modify for Maximum Spanning Tree?
A11: Change minimum finding logic to maximum:
     - Replace min_weight = float('inf') with max_weight = float('-inf')
     - Change condition: weight > max_weight instead of weight < min_weight
     - Same algorithm structure, opposite optimization objective

Q12: Handle case where graph has no edges?
A12: Algorithm handles gracefully:
     - If no edges from start vertex: min_edge remains None
     - Algorithm terminates with empty MST
     - Result: MST has 0 edges, represents single isolated vertex

Q13: How to track which vertices are reachable?
A13: Check size of visited set after algorithm completes:
     - If len(visited) == len(graph): all vertices reachable
     - If len(visited) < len(graph): graph is disconnected
     - visited set contains all reachable vertices from start

Q14: Modify to return MST as adjacency list instead of edge list?
A14: Build adjacency representation during algorithm:
     ```python
     def prim_adjacency(graph):
         # ... existing algorithm ...
         mst_graph = {node: [] for node in graph}
         
         for node1, node2, weight in mst:
             mst_graph[node1].append((node2, weight))
             mst_graph[node2].append((node1, weight))  # undirected
         
         return mst_graph, total_weight
     ```

Q15: How to find all possible MSTs when there are ties?
A15: More complex problem requiring backtracking:
     - When multiple edges have same minimum weight, explore all choices
     - Use recursive backtracking to generate all valid MSTs
     - Exponential complexity in number of ties
     - Practical only for small graphs with few ties
"""
