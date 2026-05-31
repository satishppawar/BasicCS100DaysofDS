# Day 93 - Combination Sum IV

Notebook: [93-combination-sum-iv.ipynb](./93-combination-sum-iv.ipynb)

## Basic Notes

What is Combination Sum IV?
- `Combination Sum IV` is a counting problem where order can matter, so dynamic programming is often preferred.
- A correct approach starts by defining state, transition rules, and base conditions clearly.

Core theory details:
- Pattern: counting ordered combinations via DP.
- State: dp[t] = ways to build target t.
- Complexity: O(target * len(nums)) time.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
