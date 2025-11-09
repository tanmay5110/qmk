# Kruskal's Algorithm for Minimum Spanning Tree
# Sort all edges by weight and add them if they don't form a cycle

class UnionFind:
    """Simple Union-Find (Disjoint Set) for cycle detection"""
    def __init__(self, n):
        # Initialize parent array where each node is its own parent initially
        # This represents n separate components/sets
        self.parent = list(range(n))  # [0, 1, 2, 3, ...n-1]
    
    def find(self, x):
        # Path compression: Make every node point directly to root
        # This flattens the tree structure for faster future lookups
        if self.parent[x] != x:
            # Recursively find root and compress path
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Union by connecting roots of two different components
        root_x = self.find(x)  # Find root of x's component
        root_y = self.find(y)  # Find root of y's component
        
        if root_x != root_y:
            # Different components - safe to union (no cycle)
            self.parent[root_x] = root_y  # Make y's root the parent
            return True  # Union successful
        return False  # Same component - would create cycle

def kruskal(num_nodes, edges):
    """
    Kruskal's MST Algorithm Implementation
    num_nodes: number of nodes (0 to num_nodes-1)
    edges: list of (node1, node2, weight)
    Returns: MST edges and total weight
    """
    # Step 1: Sort all edges by weight (ascending order)
    # This ensures we always pick the minimum weight edge available
    edges = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Initialize Union-Find data structure
    uf = UnionFind(num_nodes)
    mst_edges = []  # Store edges in the MST
    total_weight = 0  # Track total MST weight
    
    # Step 3: Process edges in sorted order
    for u, v, weight in edges:
        # Try to add edge if it doesn't create a cycle
        if uf.union(u, v):  # Returns True if no cycle formed
            mst_edges.append((u, v, weight))  # Add to MST
            total_weight += weight  # Update total weight
            
            # Stop when we have n-1 edges (complete MST)
            if len(mst_edges) == num_nodes - 1:
                break
    
    return mst_edges, total_weight

# Example: 5 nodes (0-4) with weighted edges
edges = [
    (0, 1, 2),  # Edge from node 0 to node 1 with weight 2
    (0, 3, 6),  # Edge from node 0 to node 3 with weight 6
    (1, 2, 3),  # Edge from node 1 to node 2 with weight 3
    (1, 3, 8),  # Edge from node 1 to node 3 with weight 8
    (1, 4, 5),  # Edge from node 1 to node 4 with weight 5
    (2, 4, 7)   # Edge from node 2 to node 4 with weight 7
]

mst, weight = kruskal(5, edges)
print("Kruskal's MST edges:")
for u, v, w in mst:
    print(f"{u} -- {v} (weight: {w})")
print(f"Total MST weight: {weight}")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
KRUSKAL'S ALGORITHM STEP-BY-STEP:

1. SORT EDGES: Sort all edges by weight in ascending order
   - Ensures we always consider the cheapest available edge next
   
2. INITIALIZE: Create Union-Find structure with n separate components
   - Each node starts as its own component
   
3. PROCESS EDGES: For each edge in sorted order:
   - Check if adding this edge creates a cycle using Union-Find
   - If no cycle: add edge to MST and union the components
   - If cycle: skip this edge
   
4. STOP: When we have (n-1) edges, MST is complete

EXAMPLE EXECUTION:
Sorted edges: [(0,1,2), (1,2,3), (1,4,5), (0,3,6), (2,4,7), (1,3,8)]

Step 1: Add (0,1,2) - Components: {0,1}, {2}, {3}, {4} ✓
Step 2: Add (1,2,3) - Components: {0,1,2}, {3}, {4} ✓  
Step 3: Add (1,4,5) - Components: {0,1,2,4}, {3} ✓
Step 4: Add (0,3,6) - Components: {0,1,2,3,4} ✓
Step 5: Skip (2,4,7) - Would create cycle in {0,1,2,4} ✗
Step 6: Skip (1,3,8) - Would create cycle in {0,1,2,3,4} ✗

Final MST: [(0,1,2), (1,2,3), (1,4,5), (0,3,6)] with total weight 16
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is a Minimum Spanning Tree?
A1: A spanning tree of a weighted graph that has minimum total edge weight.
    - Connects all vertices with exactly (n-1) edges
    - No cycles (tree property)
    - Minimum possible total weight

Q2: What is the time complexity of Kruskal's algorithm?
A2: O(E log E) where E is number of edges
    - Sorting edges: O(E log E)
    - Union-Find operations: O(E α(V)) ≈ O(E) for practical purposes
    - Overall: O(E log E)

Q3: What data structure does Kruskal's algorithm use for cycle detection?
A3: Union-Find (Disjoint Set Union) data structure
    - Efficiently checks if two nodes are in same component
    - Union operation connects two components
    - Find operation returns component representative

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: How does path compression work in Union-Find?
A4: During find() operation, make every node on path point directly to root
    - Flattens tree structure
    - Reduces future find() operations to nearly O(1)
    - Implements: parent[x] = find(parent[x])

Q5: Why do we sort edges in Kruskal's algorithm?
A5: To ensure we always consider the minimum weight edge next
    - Greedy approach: locally optimal choice leads to global optimum
    - Guarantees minimum total weight in resulting MST

Q6: When does Kruskal's algorithm stop adding edges?
A6: When MST has exactly (n-1) edges
    - This connects all n vertices
    - Adding any more edges would create cycles
    - MST is complete at this point

🎯 ADVANCED LEVEL QUESTIONS:

Q7: Compare Kruskal's vs Prim's algorithm. When to use which?
A7: 
    Kruskal's:
    - Better for sparse graphs (few edges)
    - Edge-based approach
    - Requires sorting all edges
    - Good when edges are pre-sorted
    
    Prim's:
    - Better for dense graphs (many edges)  
    - Vertex-based approach
    - Grows MST from single vertex
    - Good with adjacency matrix representation

Q8: What happens if graph is disconnected in Kruskal's algorithm?
A8: Algorithm will find Minimum Spanning Forest
    - Each connected component gets its own MST
    - Total edges < (n-1)
    - Can detect disconnection by checking final edge count

Q9: How would you implement Union by Rank optimization?
A9: Attach smaller tree under root of larger tree
    - Maintain rank (approximate tree height) for each root
    - During union, make higher rank root the parent
    - Keeps trees balanced, improves performance

Q10: Can Kruskal's handle negative edge weights?
A10: Yes, algorithm works correctly with negative weights
     - Sorting still works (negative weights come first)
     - Union-Find logic unchanged
     - Result is still valid MST

🎯 IMPLEMENTATION QUESTIONS:

Q11: What if two edges have same weight?
A11: Order doesn't matter for correctness
     - Both choices lead to valid MST
     - Total weight remains same
     - Different MSTs possible but same minimum weight

Q12: How to modify for Maximum Spanning Tree?
A12: Sort edges in descending order instead of ascending
     - Change: sorted(edges, key=lambda x: x[2], reverse=True)
     - Rest of algorithm remains same
     - Results in maximum weight spanning tree

Q13: Space complexity of Kruskal's algorithm?
A13: O(V + E) space complexity
     - Union-Find parent array: O(V)
     - Storing edges: O(E)  
     - MST result storage: O(V)
"""
