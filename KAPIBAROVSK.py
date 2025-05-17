import numpy as np
from itertools import combinations
import time


def toggle_cell(grid, r, c):
    """
    Toggle all cells in row r and column c
    """
    # Create a copy of the grid
    new_grid = grid.copy()

    # Toggle row r
    new_grid[r, :] ^= 1

    # Toggle column c
    new_grid[:, c] ^= 1

    # The cell (r,c) was toggled twice, so toggle it once more
    new_grid[r, c] ^= 1

    return new_grid


def create_grids():
    """
    Create the target and current grids based on the specified dimensions
    """
    # Initialize grids with correct dimensions: 8 rows x 60 columns
    rows, cols = 8, 60

    # Create empty grids
    target_grid = np.zeros((rows, cols), dtype=int)
    current_grid = np.zeros((rows, cols), dtype=int)

    # Define the pattern for "КАПИБАРОВСК" and "ПИ АРОВСК"
    # We'll focus on the key differences, primarily the missing letters

    # These are approximate positions - in a real solution you'd extract exact positions from images
    # Define К (columns 0-3)
    target_grid[0:8, 1:5] = [
        [0, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    # Define А (columns 5-7)
    target_grid[0:8, 6:11] = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]

    # Define П (columns 12-15)
    pattern_P = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 0, 0],
    ]
    target_grid[0:8, 12:16] = pattern_P
    current_grid[0:8, 12:16] = pattern_P  # П is present in both states

    # Define И (columns 16-20)
    pattern_I = [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    target_grid[0:8, 16:21] = pattern_I
    current_grid[0:8, 16:21] = pattern_I  # И is present in both states

    # Define Б (columns 22-25)
    target_grid[0:8, 22:26] = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    # Define А (columns 27-31) - second A in КАПИБАРОВСК
    pattern_A2 = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    target_grid[0:8, 27:32] = pattern_A2
    current_grid[0:8, 27:32] = pattern_A2  # Second A is present in both states

    # Define Р (columns 32-36)
    pattern_R = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    target_grid[0:8, 32:36] = pattern_R
    current_grid[0:8, 32:36] = pattern_R  # Р is present in both states

    # Define О (columns 37-40)
    pattern_O = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    target_grid[0:8, 37:41] = pattern_O
    current_grid[0:8, 37:41] = pattern_O  # О is present in both states

    # Define В (columns 41-44)
    pattern_V = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    target_grid[0:8, 41:45] = pattern_V
    current_grid[0:8, 41:45] = pattern_V  # В is present in both states

    # Define С (columns 45-48)
    pattern_S = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    target_grid[0:8, 45:49] = pattern_S
    current_grid[0:8, 45:49] = pattern_S  # С is present in both states

    # Define К (columns 49-52) - second K in КАПИБАРОВСК
    pattern_K2 = [
        [0, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    target_grid[0:8, 49:53] = pattern_K2
    current_grid[0:8, 49:53] = pattern_K2  # Second К is present in both states

    # For the broken sign "ПИ АРОВСК", clear the areas where letters are missing
    current_grid[:, 1:5] = 0  # Clear К
    current_grid[:, 6:11] = 0  # Clear А
    current_grid[:, 22:26] = 0  # Clear Б

    return current_grid, target_grid


def solve_with_gaussian_elimination(current, target):
    """
    Solve the problem using Gaussian elimination in GF(2)
    """
    rows, cols = current.shape
    n_cells = rows * cols

    # Calculate the difference matrix
    diff = (current ^ target).flatten()

    # If no difference, no need to solve
    if not np.any(diff):
        return []

    # Create coefficient matrix
    A = np.zeros((n_cells, n_cells), dtype=int)

    # Fill the coefficient matrix - each row represents a cell's state
    # and each column represents the effect of clicking a cell
    for button in range(n_cells):
        r, c = button // cols, button % cols

        # For each cell, determine if pressing this button affects it
        for cell_r in range(rows):
            for cell_c in range(cols):
                cell_idx = cell_r * cols + cell_c

                # A cell is affected if it's in the same row or column
                if cell_r == r or cell_c == c:
                    A[cell_idx, button] ^= 1

                # The intersection point gets toggled twice, so toggle once more
                if cell_r == r and cell_c == c:
                    A[cell_idx, button] ^= 1

    # Solve the system using Gaussian elimination
    augmented = np.column_stack((A, diff))
    n = n_cells

    # Forward elimination
    print("Performing Gaussian elimination...")
    start_time = time.time()

    # Only consider rows where we need to make changes (where diff=1)
    active_rows = np.where(diff == 1)[0]
    if len(active_rows) == 0:
        return []

    # Create a reduced system with just the rows that need changes
    reduced_system = augmented[active_rows, :]
    active_n = len(active_rows)

    # Forward elimination on the reduced system
    for i in range(min(active_n, n)):
        # Find pivot
        pivot_row = None
        for j in range(i, active_n):
            if reduced_system[j, i] == 1:
                pivot_row = j
                break

        if pivot_row is None:
            continue  # No pivot in this column

        # Swap rows if needed
        if pivot_row != i:
            reduced_system[[i, pivot_row]] = reduced_system[[pivot_row, i]]

        # Eliminate below
        for j in range(i + 1, active_n):
            if reduced_system[j, i] == 1:
                reduced_system[j] = (reduced_system[j] + reduced_system[i]) % 2

    # Back substitution
    solution = np.zeros(n, dtype=int)

    # Process in reverse
    for i in range(min(active_n, n) - 1, -1, -1):
        if i < n and reduced_system[i, i] == 1:
            solution[i] = reduced_system[i, n]

            # Substitute back
            for j in range(i + 1, n):
                if reduced_system[i, j] == 1:
                    solution[i] = (solution[i] + solution[j]) % 2

    end_time = time.time()
    print(f"Gaussian elimination completed in {end_time - start_time:.2f} seconds")

    # Convert solution vector to coordinates
    clicks = []
    for i in range(n):
        if solution[i] == 1:
            r, c = i // cols, i % cols
            clicks.append((r, c))

    return clicks


def verify_solution(current, target, clicks):
    """
    Verify that the solution works
    """
    result = current.copy()

    for r, c in clicks:
        result = toggle_cell(result, r, c)

    return np.array_equal(result, target)


def main():
    # Create the grids
    print("Creating grids for the sign...")
    current_grid, target_grid = create_grids()

    rows, cols = current_grid.shape
    print(f"Grid dimensions: {rows} rows x {cols} columns")

    # Display a section of the grids for verification
    print("\nSection of current grid (showing part of 'ПИ АРОВСК'):")
    display_section = current_grid[:, :25]  # Show first 25 columns
    for row in display_section:
        print(''.join(['█' if cell else '·' for cell in row]))

    print("\nSection of target grid (showing part of 'КАПИБАРОВСК'):")
    display_section = target_grid[:, :25]  # Show first 25 columns
    for row in display_section:
        print(''.join(['█' if cell else '·' for cell in row]))

    # Calculate and display differences
    diff_grid = current_grid ^ target_grid
    diff_count = np.sum(diff_grid)
    print(f"\nNumber of different cells: {diff_count}")

    # Find solution using Gaussian elimination
    print("\nFinding optimal solution...")
    start_time = time.time()
    solution = solve_with_gaussian_elimination(current_grid, target_grid)
    end_time = time.time()

    if solution:
        print(f"\nSolution found with {len(solution)} clicks in {end_time - start_time:.2f} seconds!")

        print("\nCells to click:")
        for i, (r, c) in enumerate(solution):
            print(f"{i + 1}. Row {r + 1}, Column {c + 1}")

        # Verify the solution
        success = verify_solution(current_grid, target_grid, solution)
        print(f"\nVerification: {'✓ Successful' if success else '✗ Failed'}")

        if success:
            # Format for CTF submission
            print("\nFor CTF submission, use:")
            clicks_str = ";".join([f"{r},{c}" for r, c in solution])
            print(f"flag{{{clicks_str}}}")
    else:
        print("No solution found. The system might be inconsistent.")


if __name__ == "__main__":
    main()