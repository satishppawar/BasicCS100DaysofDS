# Day 84 - Word Search

Notebook: [84-word-search.ipynb](./84-word-search.ipynb)

## Basic Notes

What is Word Search?
- `Word Search` is a constraint-driven DSA problem typically solved with recursion/backtracking (or DP where applicable).
- A robust solution depends on state definition, decision choices, stopping rules, and pruning conditions.

Core theory details:
- Pattern: DFS + backtracking on grid.
- State: cell position, word index, visited mark.
- Complexity: O(R*C*4^L) worst case.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
