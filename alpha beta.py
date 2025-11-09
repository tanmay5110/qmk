board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

def print_board():
    """Display the current state of the Tic-Tac-Toe board"""
    for row in board:
        print(' '.join(row))  # Print each row with spaces between cells
    print()  # Add blank line for better readability

def is_moves_left():
    """Check if there are any empty cells left on the board"""
    for row in board:  # Iterate through each row
        if '_' in row:  # If any row contains empty cell ('_')
            return True  # Moves are still available
    return False  # No empty cells found - board is full

def evaluate():
    """Evaluate the current board state and return score
    
    Returns:
    +10: X wins (AI/Maximizer wins)
    -10: O wins (Human/Minimizer wins) 
     0: Draw or game not finished
    """
    # Check all rows for winning condition
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return 10 if board[i][0] == 'X' else -10  # Row win
    
    # Check all columns for winning condition
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return 10 if board[0][i] == 'X' else -10  # Column win
    
    # Check main diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return 10 if board[0][0] == 'X' else -10  # Diagonal win
    
    # Check anti-diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return 10 if board[0][2] == 'X' else -10  # Anti-diagonal win
    
    return 0  # No winner found - draw or game continues

def minimax(is_max, alpha, beta, depth=0):
    """Minimax algorithm with Alpha-Beta pruning
    
    Core AI algorithm that evaluates all possible game states to find optimal move
    
    Args:
    is_max: True if current player is maximizer (AI/X), False if minimizer (Human/O)
    alpha: Best value maximizer can guarantee (alpha cutoff)
    beta: Best value minimizer can guarantee (beta cutoff)  
    depth: Current depth in game tree (for move preference)
    
    Returns:
    Best score achievable from current position
    """
    # Step 1: Check if game has ended (terminal state)
    score = evaluate()
    if score == 10:     # AI wins
        return score - depth  # Prefer quicker wins (subtract depth)
    if score == -10:    # Human wins  
        return score + depth  # Prefer later losses (add depth)
    if not is_moves_left():  # Board full - draw
        return 0
    
    # Step 2: Maximizer's turn (AI trying to maximize score)
    if is_max:
        best = -1000  # Initialize to very low value
        
        # Try all possible moves
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':  # If cell is empty
                    # Make the move
                    board[i][j] = 'X'
                    
                    # Recursively evaluate this move
                    value = minimax(False, alpha, beta, depth + 1)
                    
                    # Undo the move (backtrack)
                    board[i][j] = '_'
                    
                    # Update best score found so far
                    if value > best:
                        best = value
                    
                    # Alpha-Beta pruning optimization
                    if best > alpha:
                        alpha = best  # Update alpha (maximizer's best)
                    
                    # Pruning condition: if beta <= alpha, cut off remaining branches
                    if beta <= alpha:
                        return best  # Beta cutoff - no need to explore further
        
        return best
    
    # Step 3: Minimizer's turn (Human trying to minimize score)
    else:
        best = 1000  # Initialize to very high value
        
        # Try all possible moves
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':  # If cell is empty
                    # Make the move
                    board[i][j] = 'O'
                    
                    # Recursively evaluate this move
                    value = minimax(True, alpha, beta, depth + 1)
                    
                    # Undo the move (backtrack)
                    board[i][j] = '_'
                    
                    # Update best score found so far
                    if value < best:
                        best = value
                    
                    # Alpha-Beta pruning optimization
                    if best < beta:
                        beta = best  # Update beta (minimizer's best)
                    
                    # Pruning condition: if beta <= alpha, cut off remaining branches  
                    if beta <= alpha:
                        return best  # Alpha cutoff - no need to explore further
        
        return best

def find_best_move():
    """Find the optimal move for AI using minimax algorithm"""
    best_value = -1000  # Initialize to very low value
    best_move = (-1, -1)  # Initialize to invalid position
    
    # Evaluate all possible moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':  # If cell is empty
                # Make the move temporarily
                board[i][j] = 'X'
                
                # Evaluate this move using minimax (opponent's turn next)
                move_value = minimax(False, -1000, 1000)
                
                # Undo the move
                board[i][j] = '_'
                
                # If this move is better than current best, update best move
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    
    return best_move

def reset_board():
    """Reset the board to initial empty state"""
    for i in range(3):
        for j in range(3):
            board[i][j] = '_'  # Set all cells to empty

def play_game():
    """Main game loop for human vs AI Tic-Tac-Toe"""
    reset_board()  # Start with clean board
    print("Tic-Tac-Toe: You are 'O', AI is 'X'.")
    print_board()
    
    while True:
        # Human player's turn
        try:
            row = int(input("Enter your row (1-3): ")) - 1      # Convert to 0-based index
            col = int(input("Enter your column (1-3): ")) - 1   # Convert to 0-based index
        except:
            print("Invalid input. Enter numbers 1-3.")
            continue  # Ask for input again
        
        # Validate input bounds
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Try again.")
            continue
        
        # Check if cell is already occupied
        if board[row][col] != '_':
            print("Cell occupied. Try again.")
            continue
        
        # Make human's move
        board[row][col] = 'O'
        print_board()
        
        # Check if human won
        if evaluate() == -10:
            print("You win!")
            break
        
        # Check for draw
        if not is_moves_left():
            print("Draw!")
            break
        
        # AI's turn - find and make optimal move
        move = find_best_move()
        board[move[0]][move[1]] = 'X'
        print("AI plays:")
        print_board()
        
        # Check if AI won
        if evaluate() == 10:
            print("AI wins!")
            break
        
        # Check for draw after AI's move
        if not is_moves_left():
            print("Draw!")
            break

# Main menu system
while True:
    print("Menu:")
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        play_game()
    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1 or 2.")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
MINIMAX ALGORITHM WITH ALPHA-BETA PRUNING:

PROBLEM: Create unbeatable AI for two-player zero-sum games like Tic-Tac-Toe

GAME THEORY CONCEPTS:
- Zero-sum game: one player's gain equals other player's loss
- Perfect information: both players know complete game state
- Deterministic: no random elements, outcome depends only on moves

MINIMAX STRATEGY:
- Maximizer (AI): tries to maximize game score
- Minimizer (Human): tries to minimize game score  
- Assume both players play optimally
- Recursively evaluate all possible game states

ALGORITHM STEPS:
1. If terminal state (win/lose/draw): return evaluation score
2. If maximizer's turn: choose move that maximizes score
3. If minimizer's turn: choose move that minimizes score
4. Recursively apply to all possible moves
5. Use alpha-beta pruning to eliminate unnecessary branches

ALPHA-BETA PRUNING OPTIMIZATION:
- Alpha: best value maximizer can guarantee so far
- Beta: best value minimizer can guarantee so far
- Pruning condition: if beta <= alpha, stop exploring current branch
- Intuition: if minimizer has better option elsewhere, maximizer won't choose this path

EXAMPLE GAME TREE (simplified):
                   Current Position
                  /       |        \
            Move 1      Move 2     Move 3
           /  |  \      /  |  \    /  |  \
         -1   0  +1   -1   0  +1  -1  0  +1
         
Minimax values bubble up:
- Leaves: actual game evaluations (-1, 0, +1)
- Min nodes: choose minimum of children
- Max nodes: choose maximum of children
- Root: AI chooses move leading to highest value

TIC-TAC-TOE SPECIFIC:
- Board representation: 3x3 grid with 'X', 'O', '_'
- Evaluation: +10 (AI wins), -10 (Human wins), 0 (draw)
- Depth preference: prefer quicker wins, later losses
- State space: at most 9! = 362,880 positions (much less due to early termination)

PERFORMANCE OPTIMIZATIONS:
1. Alpha-beta pruning: reduces search space significantly
2. Depth preference: score ± depth for move ordering
3. Early termination: stop when win/lose/draw detected
4. Move ordering: try corner/center moves first (not implemented here)
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is the Minimax algorithm?
A1: Decision-making algorithm for two-player zero-sum games
    - Maximizer tries to maximize score, minimizer tries to minimize
    - Assumes both players play optimally
    - Recursively evaluates all possible game states
    - Chooses move leading to best guaranteed outcome

Q2: What is Alpha-Beta pruning and why is it used?
A2: Optimization technique that eliminates branches that won't affect final decision
    - Alpha: best value maximizer can guarantee
    - Beta: best value minimizer can guarantee  
    - Prune when beta ≤ alpha (no need to explore further)
    - Can reduce search space from O(b^d) to O(b^(d/2)) in best case

Q3: How does the evaluation function work in Tic-Tac-Toe?
A3: Assigns numerical scores to terminal game states:
    - +10: AI wins (maximizer's goal)
    - -10: Human wins (minimizer's goal)
    - 0: Draw or non-terminal state
    - Depth adjustment: prefer quicker wins, delay losses

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: Why does the algorithm subtract/add depth from the score?
A4: To prefer quicker wins and later losses:
    - Win in 3 moves (score: 10-3=7) preferred over win in 5 moves (10-5=5)
    - Loss in 5 moves (score: -10+5=-5) preferred over loss in 3 moves (-10+3=-7)
    - Creates more aggressive/defensive play style

Q5: How does backtracking work in the minimax implementation?
A5: Temporary move simulation:
    1. Make move: board[i][j] = 'X' or 'O'
    2. Recursively evaluate resulting position
    3. Undo move: board[i][j] = '_'
    4. Try next possible move
    This allows exploring all possibilities without permanently changing board

Q6: What is the time complexity of minimax for Tic-Tac-Toe?
A6: O(b^d) where b=branching factor, d=depth
    - Worst case: O(9!) for complete game tree
    - With alpha-beta pruning: significantly reduced in practice
    - Tic-Tac-Toe is small enough that optimal play is always feasible

🎯 ADVANCED LEVEL QUESTIONS:

Q7: How effective is alpha-beta pruning in this implementation?
A7: Effectiveness depends on move ordering:
    - Best case: examines O(b^(d/2)) nodes instead of O(b^d)
    - Random ordering: modest improvement
    - Optimal ordering: can cut search time in half
    - This implementation could benefit from better move ordering heuristics

Q8: What game theory concepts does this algorithm demonstrate?
A8: Several key concepts:
    - Nash equilibrium: both players play optimally, outcome is predetermined
    - Backward induction: solve from end states backwards
    - Zero-sum property: AI's gain equals human's loss
    - Perfect information: complete game state visible to both players

Q9: How would you modify this for other games?
A9: Key components to change:
    - Board representation (different size/structure)
    - Move generation (legal moves function)
    - Evaluation function (game-specific scoring)
    - Terminal condition (win/lose/draw detection)
    - Depth limits (for complex games where full search infeasible)

Q10: What optimizations could improve performance further?
A10: Several advanced techniques:
     - Iterative deepening: gradually increase search depth
     - Transposition tables: cache previously computed positions
     - Move ordering: try promising moves first
     - Quiescence search: extend search in tactical positions
     - Opening book: pre-computed optimal opening moves

🎯 IMPLEMENTATION QUESTIONS:

Q11: Why use -1000 and 1000 as initial alpha/beta values?
A11: Sentinel values that ensure first real evaluation updates them:
     - Any actual game score will be better than -1000 for maximizer
     - Any actual game score will be worse than 1000 for minimizer
     - Could use float('-inf') and float('inf') for cleaner code

Q12: How to modify for games with more than 2 players?
A12: Minimax extends to multiplayer but becomes more complex:
     - Each player tries to maximize their own score
     - Evaluation returns vector of scores, one per player
     - Paranoid approach: assume all opponents cooperate against you
     - Max^n algorithm: each player maximizes own utility

Q13: What happens if evaluation function is imperfect?
A13: Algorithm finds optimal play according to evaluation function:
     - If evaluation matches true game value: perfect play
     - If evaluation is biased: suboptimal but consistent play
     - Quality of evaluation function directly affects play strength
     - For complex games, heuristic evaluation often necessary

Q14: How to handle games with chance elements (dice, cards)?
A14: Expectiminimax algorithm handles probabilistic games:
     - Add "chance nodes" between player moves
     - Expected value = sum of (probability × value) for each outcome
     - More complex than pure minimax but same principles apply

Q15: Implement move ordering to improve alpha-beta efficiency?
A15: Try moves in roughly best-to-worst order:
     ```python
     def get_ordered_moves():
         moves = []
         # Try center first (usually strong in Tic-Tac-Toe)
         if board[1][1] == '_':
             moves.append((1,1))
         # Try corners next
         for i,j in [(0,0), (0,2), (2,0), (2,2)]:
             if board[i][j] == '_':
                 moves.append((i,j))
         # Try edges last
         for i,j in [(0,1), (1,0), (1,2), (2,1)]:
             if board[i][j] == '_':
                 moves.append((i,j))
         return moves
     ```
     Better move ordering leads to more alpha-beta cutoffs
"""



Nice — let’s do this clearly and fully: first a concise theoretical explanation of **Minimax + Alpha-Beta pruning**, then a **line-by-line walkthrough** of your Tic-Tac-Toe Python code with small clarifying notes and why each bit exists. I’ll keep it practical and not too wordy, but thorough.

# Theory: Minimax + Alpha-Beta (compact & clear)

**Goal:** build an *unbeatable* AI for two-player zero-sum perfect-information games (like Tic-Tac-Toe).

* **Minimax idea:** consider the game as a tree of alternating moves.

  * **Maximizer** (AI, `X`) chooses moves to **maximize** the score.
  * **Minimizer** (human, `O`) chooses moves to **minimize** the score.
  * Leaf nodes are terminal states (win/lose/draw); their numeric values propagate up the tree. Max picks the child with largest value, Min picks smallest.
* **Alpha-Beta pruning:** same result as full minimax but skip exploring branches that cannot influence the final decision.

  * `alpha` = best (largest) value found so far along path to root for Maximizer.
  * `beta`  = best (smallest) value found so far along path to root for Minimizer.
  * If at any point `beta <= alpha`, that subtree cannot affect the final choice — prune it.

**Why depth is used in evaluation:** subtracting/adding `depth` from terminal scores breaks ties in favor of *quicker wins* or *later losses*. Example: `10 - depth` means win sooner → larger score.

**Complexity:** full minimax is O(b^d) where b=branching factor, d=depth. Alpha-Beta reduces nodes examined, sometimes dramatically, depending on move ordering.

---

# High-level pseudocode (minimax with alpha-beta)

```
function minimax(node, depth, isMax, alpha, beta):
    if node is terminal:
        return evaluate(node) adjusted by depth

    if isMax:
        best = -inf
        for each child in children(node):
            val = minimax(child, depth+1, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break   # prune
        return best
    else: # minimizer
        best = +inf
        for each child in children(node):
            val = minimax(child, depth+1, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break   # prune
        return best
```

---

# Line-by-line explanation of your code

I’ll explain each function and key blocks, in order. I’ll quote the function name, then explain relevant lines inside.

---

## Board and helpers

```python
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]
```

* `board` is a 3×3 list of lists. `'_'` denotes an empty cell. `board[i][j]` addresses row `i`, column `j`. This is the shared mutable game state.

```python
def print_board():
    for row in board:
        print(' '.join(row))
    print()
```

* Prints the board row by row with spaces between cells; an extra blank line for readability.

```python
def is_moves_left():
    for row in board:
        if '_' in row:
            return True
    return False
```

* Scans rows; returns `True` if any empty cell exists (game not yet filled). Otherwise `False`.

```python
def evaluate():
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return 10 if board[i][0] == 'X' else -10

    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return 10 if board[0][i] == 'X' else -10

    # main diagonal
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return 10 if board[0][0] == 'X' else -10

    # anti-diagonal
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return 10 if board[0][2] == 'X' else -10

    return 0
```

* `evaluate()` returns:

  * `+10` when `X` (AI) has three in a row,
  * `-10` when `O` (human) has three in a row,
  * `0` if no winner (draw or non-terminal).
* It checks rows, columns, and both diagonals in that order.

---

## minimax with alpha-beta

```python
def minimax(is_max, alpha, beta, depth=0):
    score = evaluate()
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left():
        return 0
```

* Evaluate terminal conditions first:

  * If `score == 10` (AI already won), return `10 - depth` to prefer faster wins.
  * If `score == -10`, return `-10 + depth` to prefer losses that happen later (less bad).
  * If board full and no winner, return `0` → draw.
* Note: `depth` is how many plies have been played from the original call. Using it biases solutions by move length.

### Maximizer branch (`is_max == True`)

```python
if is_max:
    best = -1000
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                value = minimax(False, alpha, beta, depth + 1)
                board[i][j] = '_'
                if value > best:
                    best = value
                if best > alpha:
                    alpha = best
                if beta <= alpha:
                    return best
    return best
```

* `best` starts very low (`-1000`) as a sentinel.
* Loop over all empty cells (legal moves).

  * Try move: set `board[i][j] = 'X'`.
  * Recursively call `minimax` for the opponent (`is_max=False`) with `depth+1`.
  * Undo move (backtrack).
  * Update `best` if `value` is higher.
  * Update `alpha` = max(current alpha, best).
  * If `beta <= alpha` then **prune**: return `best` early (no need to examine other moves).
* Returning `best` bubbles the best achievable score for the maximizer at this node.

### Minimizer branch (`is_max == False`)

```python
else:
    best = 1000
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                value = minimax(True, alpha, beta, depth + 1)
                board[i][j] = '_'
                if value < best:
                    best = value
                if best < beta:
                    beta = best
                if beta <= alpha:
                    return best
    return best
```

* Symmetric to maximizer:

  * `best` starts very high (`1000`) sentinel.
  * For each legal move, place `O`, evaluate deeper, undo.
  * Update `best = min(best, value)`.
  * Update `beta = min(beta, best)`.
  * If `beta <= alpha`, prune and return `best`.

**Important to note:** returning immediately on pruning is fine because that branch cannot affect parent choices due to alpha/beta bounds.

---

## find_best_move()

```python
def find_best_move():
    best_value = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_value = minimax(False, -1000, 1000)
                board[i][j] = '_'
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move
```

* Iterates all possible AI moves.
* Simulates putting `X` into each empty cell.
* Calls `minimax(False, -1000, 1000)` to evaluate the resulting position from the opponent's point of view (minimizer moves next). Note initial `alpha` = -1000, `beta` = 1000 are sentinel bounds.
* Records the move that yields the highest `move_value`.
* Returns the best move coordinates `(row, col)`.

**Why `-1000`/`1000`?** They’re sentinel extremes ensuring the first real evaluation will update alpha/beta. Could also use `float('-inf')` and `float('inf')`.

---

## reset_board, play_game and main menu

```python
def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = '_'
```

* Set every cell back to empty.

```python
def play_game():
    reset_board()
    print("Tic-Tac-Toe: You are 'O', AI is 'X'.")
    print_board()

    while True:
        try:
            row = int(input("Enter your row (1-3): ")) - 1
            col = int(input("Enter your column (1-3): ")) - 1
        except:
            print("Invalid input. Enter numbers 1-3.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Try again.")
            continue

        if board[row][col] != '_':
            print("Cell occupied. Try again.")
            continue

        board[row][col] = 'O'
        print_board()

        if evaluate() == -10:
            print("You win!")
            break

        if not is_moves_left():
            print("Draw!")
            break

        move = find_best_move()
        board[move[0]][move[1]] = 'X'
        print("AI plays:")
        print_board()

        if evaluate() == 10:
            print("AI wins!")
            break

        if not is_moves_left():
            print("Draw!")
            break
```

* `play_game()` loops human turn → evaluate → AI turn → evaluate until terminal.
* Human enters row & col (1..3), converted to 0-based indices.
* Input validation: bounds check and empty cell check.
* After a human move:

  * Check if human won (`evaluate() == -10`).
  * Check draw (no moves left).
* Then AI calculates `find_best_move()` and plays it; check if AI won or draw again.
* Loop ends when a terminal state is reached.

Main menu simple loop:

```python
while True:
    print("Menu:")
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        play_game()
    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1 or 2.")
```

* Repeats until user exits.

---

# Example trace (short) — why alpha-beta prunes

Suppose the AI (X) first tries center `(1,1)`. The algorithm evaluates all replies by `O`, then deeper. At some node, suppose Maximizer has already found a move with value `8` earlier; while evaluating another branch, the Minimizer finds a child with value `≤ 8` that forces `beta` to drop ≤ `alpha`. Then `beta <= alpha` occurs and the remaining moves in that subtree are skipped — they can’t raise the minimizer’s choice above the already known alternative. This saves time.

In Tic-Tac-Toe the entire tree is small, but pruning still avoids many symmetric/redundant nodes.

---

# Small implementation suggestions / improvements

1. **Use `float('-inf')` / `float('inf')`** instead of `-1000`/`1000` — clearer and safe:

   ```python
   move_value = minimax(False, float('-inf'), float('inf'))
   ```
2. **Move ordering:** try center then corners then edges; improves pruning.
3. **Use `get_ordered_moves()`** function to return moves in a good order. You included such an example in your big comment — use it inside minimax loops.
4. **Cache/evaluation micro-optimizations:** check immediate winning moves before recursion to short-circuit.
5. **Depth limit** (not necessary here) for larger games — combine with heuristic evaluation function.

---

# Quick summary (so it’s easy to remember)

* **Minimax**: examine all possible move sequences; maximizer picks max, minimizer picks min.
* **Alpha-Beta**: maintain `alpha` and `beta` bounds to prune branches that can’t change the decision. Same result as minimax, but faster.
* In your code:

  * `minimax(is_max, alpha, beta, depth)` implements Minimax + Alpha-Beta.
  * `find_best_move()` tries each first move, uses minimax to score it, picks best.
  * `evaluate()` gives terminal scores; `depth` adjusts to prefer quicker wins.
  * `board` is the shared state; moves are tried then undone (backtracking).

---

If you want, I can now:

* 1. Run a small trace of a particular starting position and show the recursion tree (manually), or
* 2. Provide a slightly refactored, cleaner version of this code with `float('-inf')`/`float('inf')`, move ordering, and comments, or
* 3. Show an annotated call example (the sequence of minimax calls for one move) step-by-step.

Which would you like next?

