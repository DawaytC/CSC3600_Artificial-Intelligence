#DWIGHT CUTAD
#213748

import heapq

class PuzzleState:
    def __init__(self, board, g, h, parent=None):
        self.board = board
        self.g = g  # Cost to reach this state
        self.h = h  # Heuristic cost to reach the goal
        self.f = g + h  # Total cost (g + h)
        self.parent = parent  # Pointer to the parent state to reconstruct the path

    def __lt__(self, other):
        return self.f < other.f  # Less-than method for priority queue (heapq)

def manhattan_distance(board, goal):
    """
    Calculate the Manhattan distance heuristic for the current board.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:  # Skip the blank tile (represented by 0)
                goal_x, goal_y = divmod(goal.index(board[i][j]), 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def generate_neighbors(state, goal):
    """
    Generate all possible neighboring states by moving the blank tile.
    """
    neighbors = []
    x, y = next((i, j) for i, row in enumerate(state.board) for j, val in enumerate(row) if val == 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right moves

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Ensure the move is within bounds
            new_board = [row[:] for row in state.board]  # Deep copy the board
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]  # Swap the blank tile
            h = manhattan_distance(new_board, goal)  # Calculate heuristic
            neighbors.append(PuzzleState(new_board, state.g + 1, h, state))  # Create new state and add to neighbors

    return neighbors

def solve_puzzle(initial_board, goal_board):
    """
    Solve the 8-puzzle using A* search algorithm.
    """
    goal_flat = [item for sublist in goal_board for item in sublist]  # Flatten the goal board for easy index lookup
    initial_state = PuzzleState(initial_board, 0, manhattan_distance(initial_board, goal_flat))  # Initial state
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, initial_state)  # Push the initial state into the priority queue

    while open_list:
        current_state = heapq.heappop(open_list)  # Pop the state with the lowest f value
        if current_state.board == goal_board:  # Goal test
            return reconstruct_path(current_state), current_state.g  # Return the solution path and total moves

        closed_set.add(tuple(map(tuple, current_state.board)))  # Add current state to the closed set

        for neighbor in generate_neighbors(current_state, goal_flat):  # Generate neighbors
            if tuple(map(tuple, neighbor.board)) in closed_set:  # Skip already visited states
                continue
            heapq.heappush(open_list, neighbor)  # Push neighbor state into the priority queue

    return None, None  # Return None if no solution is found

def reconstruct_path(state):
    """
    Reconstruct the path from the goal state to the initial state.
    """
    path = []
    while state:
        path.append(state.board)  # Append the current board to the path
        state = state.parent  # Move to the parent state
    return path[::-1]  # Return the reversed path

def print_path(path):
    """
    Print the solution path.
    """
    for step in path:
        for row in step:
            print(row)
        print()

if __name__ == "__main__":
    initial_board = [
        [2, 7, 0],
        [4, 1, 6],
        [8, 3, 5]
    ]

    goal_board = [
        [7, 6, 5],
        [8, 0, 4],
        [1, 2, 3]
    ]

    solution_path, total_moves = solve_puzzle(initial_board, goal_board)
    if solution_path:
        print("Solution found!")
        print("Total number of moves (g(n)):", total_moves)
        print_path(solution_path)
    else:
        print("No solution exists.")