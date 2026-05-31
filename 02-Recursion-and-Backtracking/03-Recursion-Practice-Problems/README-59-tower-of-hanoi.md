# Day 59 - Tower of Hanoi

Notebook: [59-tower-of-hanoi.ipynb](./59-tower-of-hanoi.ipynb)

## Basic Notes

What is Tower of Hanoi?
- `Tower of Hanoi` is a constraint-driven DSA problem typically solved with recursion/backtracking (or DP where applicable).
- A robust solution depends on state definition, decision choices, stopping rules, and pruning conditions.

Core theory details:
- Pattern: classic recursion with 2 subproblems + 1 move.
- State: number of disks and 3 rods.
- Complexity: O(2^n) time, O(n) recursion depth.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
