# Prim's Algorithm for Minimum Spanning Tree
# Start from any vertex and grow the MST by adding minimum edge

def prim(graph, start):
    """
    Prim's MST Algorithm Implementation
    graph: adjacency list {node: [(neighbor, weight), ...]}
    start: starting node
    Returns: MST edges and total weight
    """
    # Initialize visited set with starting node
    # Prim's grows MST by adding one vertex at a time
    visited = set([start])
    
    mst_edges = []  # Store MST edges as we build the tree
    total_weight = 0  # Track cumulative weight of MST
    nodes = set(graph.keys())  # All nodes in the graph
    
    # Continue until all nodes are included in MST
    while len(visited) < len(nodes):
        min_edge = None  # Track minimum weight edge found
        min_weight = float('inf')  # Initialize to infinity
        
        # Find cheapest edge from visited to unvisited nodes
        # This is the key step: always pick minimum crossing edge
        for node in visited:  # For each node already in MST
            for neighbor, weight in graph.get(node, []):  # Check its neighbors
                # Only consider edges to unvisited nodes (crossing edges)
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight  # Update minimum weight
                    min_edge = (node, neighbor, weight)  # Store the edge
        
        # If no edge found, graph might be disconnected
        if min_edge is None:
            break
        
        # Add the minimum edge to MST
        u, v, w = min_edge
        mst_edges.append(min_edge)  # Add edge to MST
        visited.add(v)  # Mark destination vertex as visited
        total_weight += w  # Add weight to total
    
    return mst_edges, total_weight

# Example graph represented as adjacency list
# Each node maps to list of (neighbor, weight) tuples
graph = {
    0: [(1, 2), (3, 6)],      # Node 0 connects to: node 1 (weight 2), node 3 (weight 6)
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],  # Node 1's connections
    2: [(1, 3), (4, 7)],      # Node 2's connections  
    3: [(0, 6), (1, 8)],      # Node 3's connections
    4: [(1, 5), (2, 7)]       # Node 4's connections
}

edges, weight = prim(graph, 0)  # Start MST construction from node 0
print("Prim's MST edges:")
for u, v, w in edges:
    print(f"{u} -- {v} (weight: {w})")
print(f"Total MST weight: {weight}")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
PRIM'S ALGORITHM STEP-BY-STEP:

1. START: Begin with any vertex (arbitrary choice)
   - Mark starting vertex as visited
   - MST initially contains just this vertex

2. GROW MST: Repeat until all vertices included:
   - Find minimum weight edge from visited to unvisited vertices
   - Add this edge to MST
   - Mark destination vertex as visited

3. TERMINATE: When all vertices are visited, MST is complete

EXAMPLE EXECUTION (starting from node 0):
Graph: 0--(2)--1--(3)--2
       |       |       |
      (6)     (8)     (7)
       |       |       |
       3-------(5)-----4

Step 1: Start with {0}, edges available: (0,1,2), (0,3,6)
        Choose (0,1,2) - minimum weight
        Visited: {0,1}, MST: [(0,1,2)]

Step 2: From {0,1}, edges available: (0,3,6), (1,2,3), (1,3,8), (1,4,5)
        Choose (1,2,3) - minimum weight  
        Visited: {0,1,2}, MST: [(0,1,2), (1,2,3)]

Step 3: From {0,1,2}, edges available: (0,3,6), (1,3,8), (1,4,5), (2,4,7)
        Choose (1,4,5) - minimum weight
        Visited: {0,1,2,4}, MST: [(0,1,2), (1,2,3), (1,4,5)]

Step 4: From {0,1,2,4}, edges available: (0,3,6), (1,3,8)
        Choose (0,3,6) - minimum weight
        Visited: {0,1,2,3,4}, MST: [(0,1,2), (1,2,3), (1,4,5), (0,3,6)]

Final MST weight: 2 + 3 + 5 + 6 = 16
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is the main idea behind Prim's algorithm?
A1: Grow MST incrementally by always adding the minimum weight edge
    that connects a visited vertex to an unvisited vertex.
    - Start with any vertex
    - Always choose cheapest "crossing edge"
    - Grows MST one vertex at a time

Q2: What is the time complexity of basic Prim's algorithm?
A2: O(V²) for the basic implementation shown
    - Outer loop runs V times (until all vertices visited)
    - Inner loops scan all edges to find minimum: O(V + E)
    - Total: O(V × (V + E)) = O(V²) for dense graphs

Q3: How does Prim's differ from Kruskal's algorithm?
A3: 
    Prim's: Vertex-centric, grows connected MST from single vertex
    Kruskal's: Edge-centric, considers all edges globally
    
    Prim's: Good for dense graphs, uses adjacency lists well
    Kruskal's: Good for sparse graphs, requires edge sorting

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: Can Prim's algorithm start from any vertex?
A4: Yes, starting vertex doesn't affect final MST weight
    - Different starting points may produce different MSTs
    - But all valid MSTs have same minimum total weight
    - Choice of start vertex is arbitrary

Q5: What data structures can optimize Prim's algorithm?
A5: Priority Queue (Min-Heap) for better performance
    - Store edges with priorities as weights
    - Extract minimum weight edge in O(log E) time
    - Overall complexity becomes O(E log V)

Q6: How does Prim's handle disconnected graphs?
A6: Algorithm terminates when no more edges found
    - Produces MST for connected component containing start vertex
    - Other components remain unconnected
    - Can detect disconnection by checking final vertex count

🎯 ADVANCED LEVEL QUESTIONS:

Q7: Implement Prim's with priority queue - what changes?
A7: Replace linear search with heap operations:
    - Use heapq to maintain edge priorities
    - Push all edges from newly added vertex to heap
    - Pop minimum edge and check if destination unvisited
    - Reduces time complexity to O(E log V)

Q8: Why is Prim's algorithm greedy? Prove it works.
A8: Greedy: Always picks locally optimal choice (minimum edge)
    Proof by cut property:
    - Consider any cut separating visited from unvisited vertices
    - Minimum edge across cut must be in some MST
    - Prim's always chooses this minimum edge
    - Therefore, Prim's choices are always optimal

Q9: Compare space complexity: Prim's vs Kruskal's?
A9: 
    Prim's: O(V) space
    - visited set: O(V)
    - No need to store all edges simultaneously
    
    Kruskal's: O(V + E) space  
    - Union-Find structure: O(V)
    - Must store all edges for sorting: O(E)

Q10: How to modify Prim's for Maximum Spanning Tree?
A10: Change minimum finding logic to maximum:
     - Replace min_weight = float('inf') with max_weight = float('-inf')
     - Change condition: weight > max_weight instead of weight < min_weight
     - Algorithm structure remains identical

🎯 IMPLEMENTATION QUESTIONS:

Q11: What happens if graph has negative edge weights?
A11: Algorithm still works correctly
     - Minimum finding logic handles negative weights
     - Negative edges get higher priority (selected first)
     - Result is valid MST with minimum total weight

Q12: Handle case when multiple edges have same minimum weight?
A12: Algorithm works correctly with ties
     - Any choice among equal-weight edges is valid
     - Different executions may pick different edges
     - All resulting MSTs have same total weight

Q13: How to track parent pointers for path reconstruction?
A13: Modify to store parent information:
     - Add parent dictionary: parent[v] = u when adding edge (u,v)
     - Can reconstruct MST structure from parent pointers
     - Useful for applications needing tree structure

Q14: Detect if graph is connected using Prim's?
A14: Check if len(visited) == len(nodes) after algorithm
     - If equal: graph is connected
     - If less: graph has multiple components
     - Simple connectivity test as side effect

Q15: Early termination optimization?
A15: Stop when specific target vertex reached (for some applications)
     - Not applicable for full MST construction
     - Useful for modified problems like "minimum cost to connect specific nodes"
"""
