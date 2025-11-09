# Dijkstra's Algorithm - Single Source Shortest Path Algorithm
# Find shortest path from source to all other nodes in weighted graph

def dijkstra(graph, start):
    """
    Dijkstra's Shortest Path Algorithm Implementation
    graph: adjacency list {node: [(neighbor, weight), ...]}
    start: starting node (source vertex)
    Returns: dictionary of shortest distances and predecessor paths
    """
    # Get all nodes in the graph for initialization
    nodes = set(graph.keys())
    
    # Step 1: Initialize distances - all nodes start with infinite distance except source
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0  # Distance from source to itself is 0
    
    # Initialize predecessor tracking for path reconstruction
    previous = {node: None for node in nodes}
    
    # Unvisited set - initially contains all nodes
    # We'll remove nodes as we finalize their shortest distances
    unvisited = nodes.copy()
    
    # Main algorithm loop - continue until all nodes processed
    while unvisited:
        # Step 2: Select unvisited node with minimum distance
        # This is the greedy choice - always process closest unvisited node
        current = min(unvisited, key=lambda node: distances[node])
        
        # If minimum distance is infinity, remaining nodes are unreachable
        if distances[current] == float('inf'):
            break  # All remaining nodes are disconnected from source
        
        # Step 3: Mark current node as visited (remove from unvisited set)
        unvisited.remove(current)
        
        # Step 4: Update distances to all neighbors of current node
        for neighbor, weight in graph.get(current, []):
            # Calculate new potential distance through current node
            distance = distances[current] + weight
            
            # Step 5: Relaxation - if new path is shorter, update distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Update shortest distance
                previous[neighbor] = current    # Update predecessor for path reconstruction
    
    return distances, previous

def get_path(previous, start, end):
    """Reconstruct shortest path from start to end using predecessor information"""
    path = []  # Will store the path in reverse order initially
    current = end  # Start from destination and work backwards
    
    # Follow predecessor links back to source
    while current is not None:
        path.append(current)  # Add current node to path
        current = previous[current]  # Move to predecessor
    
    # Reverse path to get correct order (source to destination)
    path.reverse()
    
    # Return path only if it starts with source (i.e., end is reachable from start)
    return path if path[0] == start else []

# Example weighted graph represented as adjacency list
# Each node maps to list of (neighbor, weight) tuples
graph = {
    'A': [('B', 4), ('C', 2)],      # A connects to B(weight=4), C(weight=2)
    'B': [('C', 1), ('D', 5)],      # B connects to C(weight=1), D(weight=5)
    'C': [('D', 8), ('E', 10)],     # C connects to D(weight=8), E(weight=10)
    'D': [('E', 2), ('F', 6)],      # D connects to E(weight=2), F(weight=6)
    'E': [('F', 3)],                # E connects to F(weight=3)
    'F': []                         # F has no outgoing edges
}

start = 'A'  # Source vertex
distances, previous = dijkstra(graph, start)

print(f"Dijkstra's shortest paths from {start}:")
print("=" * 50)
for node in sorted(distances.keys()):
    if distances[node] != float('inf'):
        path = get_path(previous, start, node)
        print(f"{start} -> {node}: distance = {distances[node]:2}, path = {' -> '.join(path)}")
    else:
        print(f"{start} -> {node}: UNREACHABLE")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
DIJKSTRA'S ALGORITHM STEP-BY-STEP:

PROBLEM: Find shortest path from source vertex to all other vertices in weighted graph

KEY INSIGHT: Greedy approach - always process the closest unvisited vertex next
This ensures when we visit a vertex, we've found its shortest path

ALGORITHM STEPS:
1. Initialize all distances to infinity, source distance to 0
2. While unvisited vertices remain:
   a. Select unvisited vertex with minimum distance
   b. Mark it as visited  
   c. Update distances to all its neighbors (relaxation)
3. Result: shortest distances from source to all vertices

EXAMPLE EXECUTION (from vertex A):

Initial: dist[A]=0, dist[B]=∞, dist[C]=∞, dist[D]=∞, dist[E]=∞, dist[F]=∞

Step 1: Process A (closest unvisited: distance=0)
        Update neighbors: B=4, C=2
        dist = {A:0, B:4, C:2, D:∞, E:∞, F:∞}

Step 2: Process C (closest unvisited: distance=2)  
        Update neighbors: D=min(∞,2+8)=10, E=min(∞,2+10)=12
        dist = {A:0, B:4, C:2, D:10, E:12, F:∞}

Step 3: Process B (closest unvisited: distance=4)
        Update neighbors: C=min(2,4+1)=2, D=min(10,4+5)=9
        dist = {A:0, B:4, C:2, D:9, E:12, F:∞}

Step 4: Process D (closest unvisited: distance=9)
        Update neighbors: E=min(12,9+2)=11, F=min(∞,9+6)=15
        dist = {A:0, B:4, C:2, D:9, E:11, F:15}

Step 5: Process E (closest unvisited: distance=11)
        Update neighbors: F=min(15,11+3)=14
        dist = {A:0, B:4, C:2, D:9, E:11, F:14}

Step 6: Process F (closest unvisited: distance=14)
        No neighbors to update
        Final: dist = {A:0, B:4, C:2, D:9, E:11, F:14}

Shortest paths:
A->A: 0 (A)
A->B: 4 (A->B)  
A->C: 2 (A->C)
A->D: 9 (A->B->D)
A->E: 11 (A->B->D->E)
A->F: 14 (A->B->D->E->F)
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What problem does Dijkstra's algorithm solve?
A1: Single-Source Shortest Path problem in weighted graphs
    - Finds shortest path from one source vertex to all other vertices
    - Works only with non-negative edge weights
    - Produces shortest distance and actual path

Q2: What is the time complexity of Dijkstra's algorithm?
A2: O(V²) for basic implementation, O((V+E) log V) with priority queue
    - Basic: O(V) iterations × O(V) to find minimum = O(V²)
    - With min-heap: O(V) extractions × O(log V) + O(E) relaxations × O(log V)
    - Priority queue version better for sparse graphs

Q3: Why doesn't Dijkstra work with negative edge weights?
A3: Greedy assumption breaks down with negative weights
    - Algorithm assumes once a vertex is visited, its shortest path is final
    - Negative edges could create shorter paths through "longer" routes
    - Use Bellman-Ford algorithm for graphs with negative weights

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: What is the relaxation step in Dijkstra's algorithm?
A4: Process of updating distance to a vertex if shorter path found
    - Compare current known distance vs. distance through current vertex
    - If distance[current] + weight < distance[neighbor]:
      update distance[neighbor] and previous[neighbor]
    - Name comes from "relaxing" the upper bound on shortest distance

Q5: How do you reconstruct the actual shortest path?
A5: Use predecessor array (previous) to backtrack from destination
    - Start from destination vertex
    - Follow previous[vertex] links back to source
    - Reverse the resulting path
    - Path exists only if destination is reachable from source

Q6: What happens if graph has multiple shortest paths of same length?
A6: Algorithm finds one valid shortest path (not necessarily unique)
    - Different execution orders may find different paths
    - All found paths have same minimum total weight
    - Can modify to find all shortest paths or lexicographically smallest

🎯 ADVANCED LEVEL QUESTIONS:

Q7: Compare Dijkstra's with other shortest path algorithms?
A7: 
    Dijkstra's: Single-source, non-negative weights, O(V²) or O((V+E)log V)
    Bellman-Ford: Single-source, allows negative weights, O(VE), detects negative cycles
    Floyd-Warshall: All-pairs shortest paths, O(V³), handles negative weights
    A*: Single-source to single-destination, uses heuristic, faster for specific targets

Q8: How to implement Dijkstra's with priority queue for better performance?
A8: Replace linear search with min-heap:
    - Use heapq.heappush() to add (distance, vertex) pairs
    - Use heapq.heappop() to extract minimum distance vertex
    - Handle duplicate entries by checking if vertex already visited
    - Reduces time complexity to O((V+E) log V)

Q9: What is the correctness proof of Dijkstra's algorithm?
A9: Proof by induction on set of visited vertices:
    - Base: Source vertex has correct shortest distance (0)
    - Inductive step: When visiting vertex u, distance[u] is optimal
    - Key insight: Any shorter path to u would go through unvisited vertex v
    - But then distance[v] < distance[u], contradicting choice of u as minimum
    - Therefore, greedy choice always yields optimal substructure

Q10: How does Dijkstra handle disconnected graphs?
A10: Algorithm correctly handles disconnected components:
     - Unreachable vertices maintain infinite distance
     - Algorithm terminates when minimum distance is infinite
     - Can detect unreachable vertices by checking for infinite distances
     - Each connected component processed independently

🎯 IMPLEMENTATION QUESTIONS:

Q11: How to modify Dijkstra to stop when target vertex is reached?
A11: Add termination condition in main loop:
     - if current == target: break
     - More efficient for single-destination queries
     - Still guarantees optimal solution due to greedy property

Q12: What if graph has self-loops or multiple edges?
A12: Algorithm handles these correctly:
     - Self-loops: ignored if weight ≥ 0 (can't improve shortest path)
     - Multiple edges: only shortest edge between vertices matters
     - Can preprocess to remove redundant edges

Q13: How to track number of shortest paths to each vertex?
A13: Add count array alongside distances:
     - count[start] = 1, count[others] = 0
     - During relaxation: if distance equals current best, add counts
     - If distance better than current best, reset count to count[current]

Q14: Implement bidirectional Dijkstra for faster single-target search?
A14: Run Dijkstra from both source and target simultaneously:
     - Alternate between forward and backward search
     - Stop when searches meet (vertex visited by both)
     - Reconstruct path by combining forward and backward paths
     - Can be significantly faster for long paths

Q15: How to find k-shortest paths using Dijkstra's?
A15: Use Yen's algorithm or modify with k-shortest paths data structure:
     - Find shortest path with standard Dijkstra's
     - For each intermediate vertex, find shortest path avoiding that vertex
     - Maintain priority queue of candidate k-shortest paths
     - More complex but builds on Dijkstra's foundation
"""
