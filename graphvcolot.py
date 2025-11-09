# Graph Coloring using Backtracking
# Constraint Satisfaction Problem: Color graph vertices so no adjacent vertices share a color

def is_safe(graph, colors, vertex, color):
    """Check if assigning 'color' to 'vertex' is safe"""
    # Iterate through all vertices to check adjacency
    for i in range(len(graph)):
        # Check if vertex i is adjacent to current vertex AND has same color
        # graph[vertex][i] == 1 means there's an edge between vertex and i
        # colors[i] == color means vertex i already has the color we want to assign
        if graph[vertex][i] == 1 and colors[i] == color:
            return False  # Conflict found - not safe to assign this color
    return True  # No conflicts - safe to assign this color

def graph_coloring(graph, m, colors, vertex):
    """Backtracking function to color the graph
    
    graph: adjacency matrix representation of the graph
    m: number of colors available (1, 2, 3, ..., m)
    colors: array storing color of each vertex (0 means uncolored)
    vertex: current vertex being colored (0 to n-1)
    """
    # Base case: all vertices have been successfully colored
    if vertex == len(graph):
        return True  # Solution found!
    
    # Try all available colors for the current vertex
    for color in range(1, m + 1):  # Colors numbered from 1 to m
        # Check if assigning this color to current vertex is safe
        if is_safe(graph, colors, vertex, color):
            # Safe to assign - make the assignment
            colors[vertex] = color
            
            # Recursively try to color the remaining vertices
            if graph_coloring(graph, m, colors, vertex + 1):
                return True  # Solution found in recursive call
            
            # Backtrack: remove the color assignment if no solution found
            colors[vertex] = 0  # Reset to uncolored state
    
    # No valid color found for this vertex with current partial solution
    return False

# ===== USER INPUT SECTION =====
print("=" * 50)
print("GRAPH COLORING PROBLEM - BACKTRACKING")
print("=" * 50)

# Get number of vertices from user
V = int(input("\nEnter number of vertices: "))

# Create adjacency matrix: graph[i][j] = 1 if edge exists between i and j
graph = [[0 for _ in range(V)] for _ in range(V)]

# Get number of edges from user
E = int(input("Enter number of edges: "))
print(f"\nEnter {E} edges (format: vertex1 vertex2)")
print("Note: Vertices are numbered from 0 to", V-1)

# Input each edge and create undirected graph
for i in range(E):
    u, v = map(int, input(f"Edge {i+1}: ").split())
    # Create undirected edge: if u connects to v, then v connects to u
    graph[u][v] = 1  # Edge from u to v
    graph[v][u] = 1  # Edge from v to u (undirected)

# Get number of colors available
m = int(input("\nEnter number of colors available: "))

# Initialize colors array: 0 means uncolored
colors = [0] * V

print("\n" + "=" * 50)
print("SOLVING...")
print("=" * 50)

# Solve the graph coloring problem
if graph_coloring(graph, m, colors, 0):
    print("\n✓ Solution found!")
    print("\nVertex -> Color Assignment:")
    print("-" * 30)
    for i in range(V):
        print(f"Vertex {i} -> Color {colors[i]}")
    
    print("\n" + "=" * 50)
    print("VERIFICATION:")
    print("=" * 50)
    # Verify the solution by checking all constraints
    valid = True
    for i in range(V):
        for j in range(V):
            # If there's an edge between i and j, they shouldn't have same color
            if graph[i][j] == 1 and colors[i] == colors[j]:
                print(f"✗ ERROR: Adjacent vertices {i} and {j} have same color!")
                valid = False
    if valid:
        print("✓ All constraints satisfied!")
        print(f"✓ Graph successfully colored with {m} colors")
else:
    print(f"\n✗ No solution exists with {m} colors")
    print(f"Try increasing the number of colors")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
GRAPH COLORING BACKTRACKING ALGORITHM:

PROBLEM: Assign colors to vertices such that no two adjacent vertices have the same color

APPROACH: 
1. Try to color vertices one by one (0, 1, 2, ..., n-1)
2. For each vertex, try all available colors (1, 2, ..., m)
3. Check if current color assignment is safe (no adjacent vertex has same color)
4. If safe, assign color and recursively solve for next vertex
5. If recursive call succeeds, solution found
6. If recursive call fails, backtrack by removing color and try next color
7. If no color works for current vertex, return false (backtrack further)

EXAMPLE EXECUTION:
Graph: 0---1---2 (triangle: 0-1-2-0)
       |       |
       -------

Colors available: 3 (Red=1, Blue=2, Green=3)

Step 1: Color vertex 0
   Try color 1: Safe ✓ → colors = [1, 0, 0]
   
Step 2: Color vertex 1  
   Try color 1: Conflicts with vertex 0 ✗
   Try color 2: Safe ✓ → colors = [1, 2, 0]
   
Step 3: Color vertex 2
   Try color 1: Conflicts with vertex 0 ✗
   Try color 2: Conflicts with vertex 1 ✗  
   Try color 3: Safe ✓ → colors = [1, 2, 3]
   
All vertices colored successfully!
Final solution: Vertex 0=Red, Vertex 1=Blue, Vertex 2=Green
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is the Graph Coloring Problem?
A1: Assign colors to vertices of a graph such that no two adjacent 
    vertices have the same color, using minimum number of colors.
    - NP-Complete problem
    - Applications: scheduling, register allocation, frequency assignment

Q2: What is the chromatic number of a graph?
A2: Minimum number of colors needed to properly color the graph.
    - Complete graph Kn: chromatic number = n
    - Tree with n>1 vertices: chromatic number = 2
    - Cycle with odd length: chromatic number = 3
    - Cycle with even length: chromatic number = 2

Q3: What is backtracking and why use it here?
A3: Systematic trial-and-error approach that undoes choices when they lead to dead ends.
    - Try all possibilities systematically
    - Undo (backtrack) when current path fails
    - Guarantees finding solution if one exists
    - Better than brute force: prunes impossible branches early

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: What is the time complexity of backtracking graph coloring?
A4: O(m^V) in worst case, where m = colors, V = vertices
    - Each vertex can be assigned m different colors
    - V vertices to color
    - Exponential complexity but practical for small graphs

Q5: How does the is_safe() function work?
A5: Checks constraint satisfaction for current color assignment
    - Examines all vertices adjacent to current vertex
    - Returns false if any adjacent vertex has same color
    - Uses adjacency matrix: graph[i][j] = 1 means edge exists

Q6: What optimizations can improve backtracking performance?
A6: Several heuristics:
    - Most Constrained Variable: color vertex with fewest available colors first
    - Least Constraining Value: choose color that rules out fewest options for neighbors
    - Forward Checking: propagate constraints to reduce future search space
    - Arc Consistency: maintain consistency between related variables

🎯 ADVANCED LEVEL QUESTIONS:

Q7: Compare different graph representations for coloring?
A7: 
    Adjacency Matrix (used here):
    + Simple constraint checking: O(1) edge lookup
    + Easy to implement
    - Space: O(V²) even for sparse graphs
    
    Adjacency List:
    + Space efficient: O(V + E)
    - Constraint checking: O(degree) per vertex
    + Better for sparse graphs

Q8: How to find the chromatic number of a graph?
A8: Try k-coloring for k = 1, 2, 3, ... until solution found
    - Binary search optimization: try between lower/upper bounds
    - Lower bound: size of maximum clique
    - Upper bound: maximum degree + 1 (Brooks' theorem)

Q9: What is the Welsh-Powell algorithm alternative?
A9: Greedy approximation algorithm:
    1. Sort vertices by degree (descending)
    2. Color vertices in order using first available color
    3. Fast O(V²) but may not find optimal coloring
    4. Good for getting upper bound on chromatic number

Q10: How does graph coloring relate to other problems?
A10: Equivalent formulations:
     - Scheduling: vertices = tasks, edges = conflicts, colors = time slots
     - Register Allocation: vertices = variables, edges = interference, colors = registers  
     - Frequency Assignment: vertices = transmitters, edges = interference, colors = frequencies
     - Sudoku: vertices = cells, edges = same row/column/box, colors = numbers

🎯 IMPLEMENTATION QUESTIONS:

Q11: How to modify for minimum coloring (find chromatic number)?
A11: Binary search on number of colors:
     - Try k-coloring for k = lower_bound to upper_bound
     - Use binary search to find minimum k where solution exists
     - More efficient than trying k = 1, 2, 3, ...

Q12: Handle case where graph is disconnected?
A12: Algorithm works correctly:
     - Each connected component can be colored independently
     - Total colors needed = max(colors needed per component)
     - Backtracking will find valid coloring for each component

Q13: How to generate all possible colorings?
A13: Modify to continue search after finding solution:
     - Don't return True immediately when solution found
     - Store current solution and continue backtracking
     - Collect all valid colorings in a list

Q14: What if we want exactly k colors (not at most k)?
A14: Add constraint to use all k colors:
     - After finding solution, verify all colors 1 to k are used
     - If not, backtrack and try different assignment
     - Or use different backtracking strategy

Q15: How to add constraint: specific vertex must have specific color?
A15: Pre-assign required colors before starting backtracking:
     - Set colors[vertex] = required_color
     - Start backtracking from next uncolored vertex
     - Constraint automatically satisfied in is_safe() checks
"""
