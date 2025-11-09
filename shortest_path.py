# Single-Source Shortest Path - using Dijkstra's algorithm
# Find shortest path from one source to all other nodes in weighted graph

def dijkstra_shortest_path(graph, start):
    """
    Single-Source Shortest Path using Dijkstra's Algorithm
    
    This is a simplified version of Dijkstra's algorithm that finds shortest
    distances from a source node to all other nodes in a weighted graph.
    
    graph: dict where graph[node] = [(neighbor, weight), ...]
    start: starting node (source vertex)
    Returns: dict of shortest distances from start to each node
    """
    # Step 1: Initialize distances dictionary
    # Set all distances to infinity except start node (distance = 0)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance from start to itself is 0
    
    # Step 2: Initialize visited set to track processed nodes
    visited = set()  # Nodes whose shortest distances are finalized
    
    # Step 3: Main algorithm loop - process nodes until all are visited
    while len(visited) < len(graph):
        # Step 4: Find unvisited node with minimum distance (greedy choice)
        min_node = None      # Node with minimum distance
        min_dist = float('inf')  # Minimum distance found so far
        
        # Linear search for minimum distance node among unvisited nodes
        for node in graph:
            if node not in visited and distances[node] < min_dist:
                min_dist = distances[node]  # Update minimum distance
                min_node = node             # Update minimum distance node
        
        # Step 5: If no reachable unvisited node found, break
        if min_node is None:
            break  # Remaining nodes are unreachable from start
        
        # Step 6: Mark current node as visited (shortest distance finalized)
        visited.add(min_node)
        
        # Step 7: Relaxation - update distances to neighbors of current node
        for neighbor, weight in graph[min_node]:
            # Calculate new potential distance through current node
            new_dist = distances[min_node] + weight
            
            # If new path is shorter, update the distance
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist  # Update shortest distance
    
    return distances

# Example weighted graph - adjacency list representation
# Each node maps to list of (neighbor, weight) tuples
graph = {
    'A': [('B', 4), ('C', 2)],      # A connects to B(weight=4), C(weight=2)
    'B': [('C', 1), ('D', 5)],      # B connects to C(weight=1), D(weight=5)
    'C': [('D', 8), ('E', 10)],     # C connects to D(weight=8), E(weight=10)
    'D': [('E', 2)],                # D connects to E(weight=2)
    'E': []                         # E has no outgoing edges (sink node)
}

start = 'A'  # Source vertex
distances = dijkstra_shortest_path(graph, start)

print(f"Single-Source Shortest Path from {start}:")
print("=" * 40)
for node, dist in distances.items():
    if dist == float('inf'):
        print(f"{start} -> {node}: UNREACHABLE")
    else:
        print(f"{start} -> {node}: {dist}")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
SINGLE-SOURCE SHORTEST PATH - DIJKSTRA'S ALGORITHM:

PROBLEM: Find shortest distance from one source vertex to all other vertices

ALGORITHM OVERVIEW:
This is a simplified implementation of Dijkstra's algorithm that computes
shortest distances but doesn't track the actual paths.

KEY INSIGHT: Greedy approach works for shortest paths with non-negative weights
- Always process the closest unvisited vertex next
- When a vertex is processed, its shortest distance is final

STEP-BY-STEP EXECUTION (Example graph from vertex A):

Initial state:
- distances = {A: 0, B: ∞, C: ∞, D: ∞, E: ∞}
- visited = {}

Iteration 1: Process A (closest unvisited: distance=0)
- visited = {A}
- Relax A's neighbors: B=min(∞,0+4)=4, C=min(∞,0+2)=2
- distances = {A: 0, B: 4, C: 2, D: ∞, E: ∞}

Iteration 2: Process C (closest unvisited: distance=2)
- visited = {A, C}  
- Relax C's neighbors: D=min(∞,2+8)=10, E=min(∞,2+10)=12
- distances = {A: 0, B: 4, C: 2, D: 10, E: 12}

Iteration 3: Process B (closest unvisited: distance=4)
- visited = {A, C, B}
- Relax B's neighbors: C=min(2,4+1)=2, D=min(10,4+5)=9
- distances = {A: 0, B: 4, C: 2, D: 9, E: 12}

Iteration 4: Process D (closest unvisited: distance=9)
- visited = {A, C, B, D}
- Relax D's neighbors: E=min(12,9+2)=11
- distances = {A: 0, B: 4, C: 2, D: 9, E: 11}

Iteration 5: Process E (closest unvisited: distance=11)
- visited = {A, C, B, D, E}
- No neighbors to relax
- Final distances = {A: 0, B: 4, C: 2, D: 9, E: 11}

SHORTEST PATHS FOUND:
A->A: 0 (trivial)
A->B: 4 (direct: A->B)
A->C: 2 (direct: A->C)  
A->D: 9 (via B: A->B->D, cost=4+5=9)
A->E: 11 (via B,D: A->B->D->E, cost=4+5+2=11)
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What problem does this algorithm solve?
A1: Single-Source Shortest Path problem in weighted graphs
    - Finds shortest distance from one source vertex to all other vertices
    - Works only with non-negative edge weights
    - This implementation returns distances only, not actual paths

Q2: How does this differ from the full Dijkstra's algorithm?
A2: This is a simplified version:
    - Computes shortest distances but doesn't track paths
    - Uses linear search instead of priority queue for minimum
    - Same correctness guarantees but less efficient: O(V²) vs O((V+E)log V)
    - Good for educational purposes and small graphs

Q3: Why use greedy approach for shortest paths?
A3: Optimal substructure property of shortest paths:
    - If shortest path from A to C goes through B, then A->B portion must be shortest path from A to B
    - Greedy choice (always process closest vertex) builds optimal solution incrementally
    - Works only with non-negative weights

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: What is the relaxation step and why is it called that?
A4: Relaxation updates distance estimate if shorter path found:
    - if distances[current] + weight < distances[neighbor]:
        distances[neighbor] = distances[current] + weight
    - Called "relaxation" because it "relaxes" the upper bound on shortest distance
    - Initially all distances are ∞ (tight upper bound), relaxation loosens them

Q5: Why doesn't this algorithm work with negative weights?
A5: Greedy assumption breaks with negative weights:
    - Algorithm assumes once vertex processed, shortest distance is final
    - Negative edges could create shorter paths through "longer" intermediate paths
    - Example: A->B=5, B->C=(-10), A->C=1. Processing A->C first misses shorter A->B->C

Q6: How to detect unreachable vertices?
A6: Check for infinite distances after algorithm completion:
    - if distances[vertex] == float('inf'): vertex unreachable
    - Also can detect by checking if min_node is None in main loop
    - Unreachable vertices remain in different connected component

🎯 ADVANCED LEVEL QUESTIONS:

Q7: What optimizations can improve this basic implementation?
A7: Several key optimizations:
    1. Priority Queue: Use min-heap instead of linear search → O((V+E)log V)
    2. Early termination: Stop when target vertex processed (single-target queries)
    3. Bidirectional search: Search from both ends simultaneously
    4. A* heuristic: Use admissible heuristic to guide search

Q8: How would you modify to return actual shortest paths?
A8: Track predecessor information during relaxation:
    ```python
    def dijkstra_with_paths(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        previous = {node: None for node in graph}  # Track predecessors
        visited = set()
        
        while len(visited) < len(graph):
            # ... find min_node as before ...
            visited.add(min_node)
            
            for neighbor, weight in graph[min_node]:
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = min_node  # Track predecessor
        
        return distances, previous
    ```

Q9: Compare this with other shortest path algorithms?
A9: 
    This simplified Dijkstra: O(V²), non-negative weights only
    Full Dijkstra: O((V+E)log V), non-negative weights only
    Bellman-Ford: O(VE), handles negative weights, detects negative cycles
    Floyd-Warshall: O(V³), all-pairs shortest paths
    A*: Heuristic-guided, faster for single target

Q10: How does graph representation affect performance?
A10: 
     Adjacency List (used here): 
     - Space: O(V + E)
     - Good for sparse graphs
     - Neighbor iteration: O(degree)
     
     Adjacency Matrix:
     - Space: O(V²)  
     - Good for dense graphs
     - Neighbor iteration: O(V)
     - Faster edge weight lookup: O(1)

🎯 IMPLEMENTATION QUESTIONS:

Q11: How to handle multiple edges between same vertices?
A11: Keep only shortest edge during preprocessing:
     - Or let algorithm handle naturally (relaxation will pick shorter)
     - Multiple edges don't break correctness, just inefficiency

Q12: Modify for maximum path instead of minimum?
A12: Change initialization and comparison:
     - distances = {node: float('-inf') for node in graph}
     - distances[start] = 0
     - if new_dist > distances[neighbor]: (instead of <)

Q13: How to find k-shortest paths?
A13: More complex - requires different approach:
     - Yen's algorithm: finds k-shortest simple paths
     - Use priority queue to maintain k-best partial paths
     - Much more complex than single shortest path

Q14: Handle graphs with self-loops?
A14: Self-loops handled naturally:
     - If self-loop weight ≥ 0: ignored (can't improve shortest path)
     - If self-loop weight < 0: invalid input (negative weight)

Q15: Convert to work with undirected graphs?
A15: Represent undirected as directed with bidirectional edges:
     ```python
     # For undirected edge (u,v) with weight w:
     graph[u].append((v, w))
     graph[v].append((u, w))
     ```
     Algorithm works unchanged on this representation
"""
