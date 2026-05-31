# Day 58 - Tail Recursion Optimization

Notebook: [58-tail-recursion-optimization.ipynb](./58-tail-recursion-optimization.ipynb)

## Basic Notes

What is Tail Recursion Optimization?
- `Tail Recursion Optimization` explains how a function solves a problem by reducing it into smaller subproblems.
- Correctness depends on a valid base case, progress toward termination, and controlled stack usage.

Core theory details:
- Some languages optimize tail calls into loops.
- Python generally does not perform TCO.
- Convert tail recursion to loop for reliability.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
