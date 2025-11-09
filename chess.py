# N-Queens Problem - Backtracking Algorithm
# Place N queens on N×N chessboard such that no two queens attack each other

def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe from attacks
    
    Queens can attack:
    1. Same row (horizontally)
    2. Same column (vertically)  
    3. Same diagonal (diagonally)
    
    board: 1D array where board[i] = column position of queen in row i
    row: current row being checked
    col: proposed column position
    n: board size (n×n)
    """
    
    # Check column conflicts with previously placed queens
    # Since we place queens row by row, we only check rows 0 to row-1
    for i in range(row):
        if board[i] == col:  # Same column - queens attack vertically
            return False
    
    # Check upper-left diagonal conflicts (\)
    # Diagonal constraint: |row1 - row2| = |col1 - col2| and same slope
    # For upper-left diagonal: row decreases as col decreases
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:  # Queen found on same upper-left diagonal
            return False
    
    # Check upper-right diagonal conflicts (/)
    # For upper-right diagonal: row decreases as col increases  
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:  # Queen found on same upper-right diagonal
            return False
    
    return True  # No conflicts found - safe to place queen

def backtracking_n_queens(n):
    """Solve N-Queens problem using backtracking
    
    BACKTRACKING STRATEGY:
    1. Try to place queens row by row (top to bottom)
    2. For each row, try all possible column positions
    3. If position is safe, place queen and recurse to next row
    4. If recursion succeeds, solution found
    5. If recursion fails, backtrack by removing queen and try next position
    6. If no position works in current row, backtrack to previous row
    
    Returns: list of all possible solutions
    """
    board = [-1] * n  # board[i] = column where queen is placed in row i (-1 = no queen)
    solutions = []    # Store all valid solutions found

    def backtrack(row):
        """Recursive backtracking function
        
        row: current row to place queen (0 to n-1)
        """
        # Base case: successfully placed queens in all rows
        if row == n:
            # All queens placed successfully - add solution to results
            solutions.append(board[:])  # Create copy of current board state
            return
        
        # Try placing queen in each column of current row
        for col in range(n):
            # Check if placing queen at (row, col) is safe
            if is_safe(board, row, col, n):
                # Safe position - place queen
                board[row] = col
                
                # Recursively try to place queens in remaining rows
                backtrack(row + 1)  # Move to next row
                
                # Backtrack: remove queen if recursive call didn't lead to solution
                board[row] = -1  # Reset position (backtrack)
                
        # If we reach here, no valid position found in this row
        # Algorithm will backtrack to previous row automatically

    # Start backtracking from row 0
    backtrack(0)
    return solutions

def print_solutions(solutions, n):
    """Print all solutions in a readable chessboard format
    
    Q = Queen position
    . = Empty square
    """
    if not solutions:
        print(f"No solutions exist for {n}-Queens problem")
        return
        
    print(f"\nFound {len(solutions)} solution(s) for {n}-Queens problem:")
    print("=" * 50)
    
    for idx, sol in enumerate(solutions):
        print(f"\nSolution {idx + 1}:")
        print("-" * (n * 2 + 1))
        
        # Print each row of the chessboard
        for r in range(n):
            row_str = "|"
            for c in range(n):
                # Place 'Q' where queen is positioned, '.' elsewhere
                if c == sol[r]:  # Queen is in column sol[r] of row r
                    row_str += "Q|"
                else:
                    row_str += ".|"
            print(row_str)
        print("-" * (n * 2 + 1))
        
        # Show solution in coordinate format
        print("Queen positions (row, col):", end=" ")
        for r in range(n):
            print(f"({r},{sol[r]})", end=" ")
        print()

# Interactive demonstration
print("N-QUEENS PROBLEM - BACKTRACKING ALGORITHM")
print("=" * 60)

# Demonstrate with different board sizes
test_cases = [4, 6, 8]

for n in test_cases:
    print(f"\n🔸 SOLVING {n}-QUEENS PROBLEM")
    print("-" * 40)
    
    solutions = backtracking_n_queens(n)
    
    if solutions:
        print(f"✓ Found {len(solutions)} solution(s)")
        # Print first solution for demonstration
        print(f"\nFirst solution for {n}×{n} board:")
        print_solutions([solutions[0]], n)
    else:
        print("✗ No solutions exist")

# Detailed walkthrough for 4-Queens
print("\n" + "=" * 60)
print("DETAILED WALKTHROUGH: 4-QUEENS PROBLEM")
print("=" * 60)

n = 4
solutions = backtracking_n_queens(n)
print_solutions(solutions, n)

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
N-QUEENS PROBLEM STEP-BY-STEP:

PROBLEM: Place N queens on N×N chessboard such that no two queens attack each other

CONSTRAINTS:
- No two queens in same row (ensured by placing one queen per row)
- No two queens in same column  
- No two queens on same diagonal (both / and \ directions)

BACKTRACKING APPROACH:
1. Place queens row by row (top to bottom)
2. For each row, try all possible columns
3. Check if current placement is safe (no conflicts)
4. If safe, place queen and recurse to next row
5. If recursion finds complete solution, record it
6. If recursion fails, backtrack by removing queen and trying next column
7. If no column works, backtrack to previous row

EXAMPLE: 4-Queens Problem Execution Tree

Row 0: Try columns 0,1,2,3
├─ Col 0: Place Q at (0,0)
│  Row 1: Try columns 0,1,2,3
│  ├─ Col 0: Conflicts with (0,0) - same column ✗
│  ├─ Col 1: Conflicts with (0,0) - same diagonal ✗  
│  ├─ Col 2: Safe ✓ Place Q at (1,2)
│  │  Row 2: Try columns 0,1,2,3
│  │  ├─ Col 0: Conflicts with (0,0) ✗
│  │  ├─ Col 1: Safe ✓ Place Q at (2,1) 
│  │  │  Row 3: Try columns 0,1,2,3 - All conflict ✗
│  │  │  Backtrack to Row 2
│  │  ├─ Col 2: Conflicts with (1,2) ✗
│  │  ├─ Col 3: Conflicts with (1,2) ✗
│  │  Backtrack to Row 1
│  └─ Col 3: Conflicts with (0,0) ✗
│  Backtrack to Row 0
├─ Col 1: Place Q at (0,1)
│  ... (similar exploration) ...
│  Eventually finds solution: [(0,1), (1,3), (2,0), (3,2)]
└─ ... Continue for remaining columns

4-Queens Solutions:
Solution 1: Q at (0,1), (1,3), (2,0), (3,2)
Solution 2: Q at (0,2), (1,0), (2,3), (3,1)

Board visualization for Solution 1:
  0 1 2 3
0 . Q . .
1 . . . Q  
2 Q . . .
3 . . Q .
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is the N-Queens problem?
A1: Classic constraint satisfaction problem: place N queens on N×N chessboard
    such that no two queens attack each other
    - Queens attack horizontally, vertically, and diagonally
    - Need to satisfy all three non-attack constraints simultaneously
    - Demonstrates backtracking algorithm principles

Q2: Why is backtracking suitable for N-Queens?
A2: N-Queens has exponential search space but many constraints:
    - Systematic exploration with early pruning
    - Can detect conflicts early and avoid exploring invalid branches  
    - Natural recursive structure (place queen in each row)
    - Ability to undo choices when they lead to dead ends

Q3: What is the time complexity of N-Queens backtracking?
A3: O(N!) in worst case, but much better in practice due to pruning
    - Without pruning: N^N possible arrangements
    - With constraint checking: approximately N! valid arrangements to check
    - Early pruning significantly reduces actual exploration

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: How does the is_safe() function work?
A4: Checks three types of conflicts for queen placement:
    1. Column conflict: board[i] == col (same column as existing queen)
    2. Upper-left diagonal: queens at (i,j) and (r,c) conflict if |i-r| = |j-c| and slope is -1
    3. Upper-right diagonal: similar check but slope is +1
    Only checks previous rows since we place queens top-to-bottom

Q5: Why use 1D array instead of 2D board representation?
A5: More efficient representation:
    - board[i] = j means queen in row i is at column j
    - Reduces space complexity from O(N²) to O(N)
    - Automatically ensures one queen per row
    - Simplifies conflict checking logic

Q6: What optimizations can improve N-Queens performance?
A6: Several optimization techniques:
    - Bit manipulation for faster conflict detection
    - Symmetry breaking: only explore half the solutions, generate rest by reflection
    - Most constrained variable heuristic: place queens in most constrained positions first
    - Forward checking: propagate constraints to reduce future search space

🎯 ADVANCED LEVEL QUESTIONS:

Q7: How many solutions exist for different values of N?
A7: Solutions count varies significantly:
    N=1: 1 solution    N=8: 92 solutions
    N=2: 0 solutions   N=9: 352 solutions  
    N=3: 0 solutions   N=10: 724 solutions
    N=4: 2 solutions   N=11: 2,680 solutions
    General formula unknown - must be computed

Q8: Implement bit manipulation optimization for N-Queens?
A8: Use three bit vectors for faster conflict detection:
    - col_mask: tracks occupied columns
    - diag1_mask: tracks occupied / diagonals  
    - diag2_mask: tracks occupied \ diagonals
    - available = ~(col_mask | diag1_mask | diag2_mask)
    - Bit operations much faster than array lookups

Q9: What is the symmetry optimization for N-Queens?
A9: Exploit board symmetries to reduce search space:
    - If solution exists, its horizontal reflection is also valid
    - Only search first N/2 columns in first row, generate symmetric solutions
    - Reduces search space by factor of 2
    - Can also use rotational symmetries for further reduction

Q10: How to modify to find just one solution instead of all?
A10: Add early termination to backtracking:
     - Return True immediately when first solution found
     - Modify recursive calls to return boolean instead of continuing search
     - Much faster when only one solution needed

🎯 IMPLEMENTATION QUESTIONS:

Q11: How to implement iterative version using stack?
A11: Replace recursion with explicit stack:
     - Stack stores (row, partial_solution) states
     - Push all valid next states onto stack
     - Pop states and continue exploration
     - More memory efficient for deep recursion

Q12: Modify to solve generalized Queens problem (different piece types)?
A12: Abstract the attack pattern:
     - Define attack_pattern() function for each piece type
     - Rooks: same row/column
     - Bishops: same diagonal
     - Knights: L-shaped moves
     - Modify is_safe() to use appropriate attack pattern

Q13: How to visualize the backtracking process?
A13: Add logging/visualization at each step:
     - Print board state before each placement
     - Show which positions are being tried
     - Indicate when backtracking occurs
     - Color-code safe/unsafe positions

Q14: Implement constraint propagation for better pruning?
A14: After placing each queen, mark all attacked positions:
     - Maintain available_positions set for each row
     - Update set after each queen placement
     - Fail early if any row has no available positions
     - Reduces search space significantly

Q15: How to solve N-Queens with additional constraints?
A15: Extend constraint checking:
     - Forbidden positions: modify is_safe() to check forbidden list
     - Required positions: pre-place queens and continue normally
     - Limited piece types: track piece counts and types
     - Modified attack patterns: update conflict detection logic
"""
