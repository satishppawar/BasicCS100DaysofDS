# Day 83 - Sudoku Solver

Notebook: [83-sudoku-solver.ipynb](./83-sudoku-solver.ipynb)

## Basic Notes

What is Sudoku Solver?
- `Sudoku Solver` is a constraint-driven DSA problem typically solved with recursion/backtracking (or DP where applicable).
- A robust solution depends on state definition, decision choices, stopping rules, and pruning conditions.

Core theory details:
- Pattern: constraint satisfaction via backtracking.
- State: empty cell index and used digits by row/col/box.
- Complexity: exponential worst case, strong pruning in practice.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
