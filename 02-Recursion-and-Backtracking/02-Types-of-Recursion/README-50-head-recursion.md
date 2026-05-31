# Day 50 - Head Recursion

Notebook: [50-head-recursion.ipynb](./50-head-recursion.ipynb)

## Basic Notes

What is Head Recursion?
- `Head Recursion` explains how a function solves a problem by reducing it into smaller subproblems.
- Correctness depends on a valid base case, progress toward termination, and controlled stack usage.

Core theory details:
- Recursive call happens before local processing.
- Work is performed during stack unwinding.
- Common in reverse-order output patterns.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
