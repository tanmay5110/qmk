from heapq import heappush, heappop
import math

class Grid:
    def __init__(self, width, height, walls=None):
        self.w = width
        self.h = height
        self.walls = set(walls) if walls else set()

    def in_bounds(self, p):
        x, y = p
        return 0 <= x < self.w and 0 <= y < self.h

    def passable(self, p):
        return p not in self.walls

    def neighbors(self, p):
        x, y = p
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            q = (x + dx, y + dy)
            if self.in_bounds(q) and self.passable(q):
                yield q

    @staticmethod
    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(parent, current):
    path = []
    s = current
    while s is not None:
        path.append(s)
        s = parent.get(s)
    path.reverse()
    return path


def astar(start, goal_test, neighbors_fn, g_cost_fn, heuristic_fn):
    """
    A* search: returns (path, cost) or (None, inf) if no path.
    """
    if goal_test(start):
        return [start], 0

    open_heap = []
    counter = 0
    g_score = {start: 0}
    parent = {start: None}
    # push (f, g, tie_counter, node)
    heappush(open_heap, (heuristic_fn(start), 0, counter, start))
    counter += 1
    closed = set()

    while open_heap:
        f, g, _, current = heappop(open_heap)
        if current in closed:
            continue
        if goal_test(current):
            return reconstruct_path(parent, current), g_score[current]
        closed.add(current)

        for nb in neighbors_fn(current):
            tentative_g = g_score[current] + g_cost_fn(current, nb)
            if nb in g_score and tentative_g >= g_score[nb]:
                continue
            # better path found
            g_score[nb] = tentative_g
            parent[nb] = current
            f_nb = tentative_g + heuristic_fn(nb)
            heappush(open_heap, (f_nb, tentative_g, counter, nb))
            counter += 1

    return None, math.inf


def best_first(start, goal_test, neighbors_fn, g_cost_fn, heuristic_fn):
    """
    Greedy Best-First Search:
    - Uses only heuristic (h) for priority.
    - Tracks parent and g_score for reporting path & cost, but priority is only heuristic.
    - Not guaranteed optimal.
    """
    if goal_test(start):
        return [start], 0

    open_heap = []
    counter = 0
    parent = {start: None}
    g_score = {start: 0}
    heappush(open_heap, (heuristic_fn(start), counter, start))
    counter += 1
    closed = set()

    while open_heap:
        h, _, current = heappop(open_heap)
        if current in closed:
            continue
        if goal_test(current):
            return reconstruct_path(parent, current), g_score[current]
        closed.add(current)

        for nb in neighbors_fn(current):
            # compute g to report cost if path found
            tentative_g = g_score[current] + g_cost_fn(current, nb)
            # If we haven't seen nb or we found a cheaper g, update parent/g_score
            if nb not in g_score or tentative_g < g_score[nb]:
                g_score[nb] = tentative_g
                parent[nb] = current
                heappush(open_heap, (heuristic_fn(nb), counter, nb))
                counter += 1

    return None, math.inf


# simple helper for unit distance
def unit_cost(a, b):
    return 1


if __name__ == '__main__':
    # ---------- interactive input (keeps same interface as your original script) ----------
    try:
        w = int(input('Enter grid width: '))
        h = int(input('Enter grid height: '))
    except ValueError:
        print("Invalid width/height. Exiting.")
        raise SystemExit

    walls_input = input('Enter wall coordinates as x1,y1 x2,y2 ... : ')
    walls = set()
    if walls_input.strip():
        for w_str in walls_input.strip().split():
            x, y = map(int, w_str.split(','))
            walls.add((x, y))

    start_x, start_y = map(int, input('Enter start coordinates x,y: ').split(','))
    goal_x, goal_y = map(int, input('Enter goal coordinates x,y: ').split(','))
    grid = Grid(w, h, walls)
    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    # run A*
    path_a, cost_a = astar(start,
                           lambda s: s == goal,
                           lambda s: grid.neighbors(s),
                           lambda a,b: unit_cost(a,b),
                           lambda s: grid.manhattan(s, goal))

    # run Best-First
    path_bf, cost_bf = best_first(start,
                                  lambda s: s == goal,
                                  lambda s: grid.neighbors(s),
                                  lambda a,b: unit_cost(a,b),
                                  lambda s: grid.manhattan(s, goal))

    print("\n=== Results ===")
    if path_a:
        print('A* Path found:', path_a)
        print('A* Total cost:', cost_a)
    else:
        print('A* No path found.')

    if path_bf:
        print('Best-First Path found:', path_bf)
        print('Best-First Total cost:', cost_bf)
    else:
        print('Best-First No path found.')




























Quick example to test (manual input)

For a 5×5 grid with a few walls, try these inputs when the program asks:

Enter grid width: → 5

Enter grid height: → 5

Enter wall coordinates as x1,y1 x2,y2 ... : → 1,1 1,2 1,3

Enter start coordinates x,y: → 0,0

Enter goal coordinates x,y: → 4,4

You’ll see both algorithms’ paths and costs printed. Often A* will give a shorter path; Best-First may take a different (not optimal) path.
