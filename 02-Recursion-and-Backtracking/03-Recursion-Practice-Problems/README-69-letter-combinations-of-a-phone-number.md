# Day 69 - Letter Combinations of a Phone Number

Notebook: [69-letter-combinations-of-a-phone-number.ipynb](./69-letter-combinations-of-a-phone-number.ipynb)

## Basic Notes

What is Letter Combinations of a Phone Number?
- `Letter Combinations of a Phone Number` is a constraint-driven DSA problem typically solved with recursion/backtracking (or DP where applicable).
- A robust solution depends on state definition, decision choices, stopping rules, and pruning conditions.

Core theory details:
- Pattern: cartesian-product generation via DFS.
- State: digit index and partial string.
- Complexity: O(3^n to 4^n) depending on digits.

Why this matters for hands-on coding:
- Implement one clean Python version and one equivalent Java version.
- Test normal, boundary, and edge cases; then document time/space complexity.

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
