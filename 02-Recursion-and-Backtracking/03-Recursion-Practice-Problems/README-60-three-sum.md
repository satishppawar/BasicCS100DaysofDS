# Day 60 - Three Sum

Notebook: [60-three-sum.ipynb](./60-three-sum.ipynb)

## Basic Notes

What is Three Sum?
- `Three Sum` is a constraint-driven DSA problem typically solved with recursion/backtracking (or DP where applicable).
- A robust solution depends on state definition, decision choices, stopping rules, and pruning conditions.

Core theory details:
- Pattern: sorting + two pointers.
- State: fixed index i and window [left, right].
- Complexity: O(n^2) time after sort, O(1) extra space.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
