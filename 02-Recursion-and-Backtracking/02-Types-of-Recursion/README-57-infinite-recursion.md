# Day 57 - Infinite Recursion

Notebook: [57-infinite-recursion.ipynb](./57-infinite-recursion.ipynb)

## Basic Notes

What is Infinite Recursion?
- `Infinite Recursion` explains how a function solves a problem by reducing it into smaller subproblems.
- Correctness depends on a valid base case, progress toward termination, and controlled stack usage.

Core theory details:
- Occurs when termination condition is unreachable.
- Common causes: wrong base case or no progress.
- Add guards and test boundary values.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
