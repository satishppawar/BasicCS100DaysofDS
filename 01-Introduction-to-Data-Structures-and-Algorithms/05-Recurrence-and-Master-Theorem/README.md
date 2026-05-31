# 05 - Recurrence Relations and Master Theorem

**Notebook:** [05-recurrence-combined-all-days.ipynb](./05-recurrence-combined-all-days.ipynb)

This folder covers mathematical techniques for analyzing recursive algorithms—expressing their cost as recurrence relations and solving them to determine complexity bounds.

## Module Overview

This section teaches you how to formally model the cost of recursive algorithms using recurrence relations and solve them using multiple techniques (Master Theorem, substitution, iteration). This is essential for analyzing divide-and-conquer algorithms and understanding deeper complexity analysis.

## Core Concepts

### What are Recurrence Relations?

`Recurrence Relations` model the cost of recursive algorithms using mathematical recurrences. The goal is to derive tight bounds that explain scalability before implementation.

**Key principles:**
- Recurrences model recursive algorithm costs
- Define clear base case(s) for valid solutions
- Solve using master/substitution/iteration methods
- Solution gives complexity bound for the recursive algorithm

**Example:** Merge sort has recurrence T(n) = 2T(n/2) + O(n), which solves to O(n log n)

### Master Theorem for Divide and Conquer

**What is the Master Theorem?**
The Master Theorem provides a direct formula for solving recurrences of the form:

T(n) = aT(n/b) + f(n)

where:
- `a` = number of recursive subproblems
- `b` = factor by which problem size is reduced
- `f(n)` = cost of combining solutions

**How it works:**
1. Identify parameters: a, b, and f(n)
2. Compute critical value: n^(log_b a)
3. Compare f(n) with n^(log_b a) to determine case
4. Apply the appropriate case to get tight bound

**Typical applications:**
- Merge sort (a=2, b=2, f(n)=O(n)) → O(n log n)
- Binary search (a=1, b=2, f(n)=O(1)) → O(log n)
- Quick sort analysis (with assumptions)
- Tree-based algorithm analysis

### Solution Methods for Recurrences

**Three main techniques:**

**1. Master Theorem (Fastest)**
- Direct formula application
- Works only for T(n) = aT(n/b) + f(n) form
- Most useful for divide-and-conquer algorithms

**2. Substitution Method (Proof)**
- Guess bound, then prove by induction-style expansion
- Verify base case and inductive step carefully
- Useful when Master Theorem does not apply directly
- More tedious but builds intuition

**3. Iteration Method (Intuition)**
- Expand recurrence repeatedly to detect pattern
- Convert to summation and simplify
- Good for building intuition before formal proof
- Shows how recurrence "unfolds" over iterations

## Hands-on Coding

For each topic:
1. Run the Python example and verify output
2. Implement or refine the Java solution for the same logic
3. Add at least 3 test cases (normal, edge, invalid/boundary)
4. Derive time and space complexity using recurrence analysis
5. Commit changes and add a short learning note

## Included Topics
## Included Topics

| Day | Topic | Description |
|---|---|---|
| 36 | Master Theorem for Divide and Conquer | Direct formula for common recurrences |
| 37 | Recurrence Relations | Modeling recursive algorithm costs |
| 38 | Solve Recurrences with Master Theorem | Applying Master Theorem to solve T(n) |
| 39 | Solve Recurrences with Substitution Method | Proof-based recurrence solving |
| 40 | Solve Recurrences with Iteration Method | Expansion-based intuitive solving |

## Suggested Study Flow

1. **Foundations (Days 36-37):** Understand recurrence form and Master Theorem
   - Learn T(n) = aT(n/b) + f(n) form
   - Understand parameters a, b, f(n)
   - See where recurrences come from

2. **Solution Techniques (Days 38-40):** Master all three methods
   - Master Theorem for quick solutions (most practical)
   - Substitution for formal proofs and edge cases
   - Iteration for building intuition

3. **Application:** Apply to analyze your own recursive algorithms
   - Model your recursion as T(n) = aT(n/b) + f(n)
   - Solve using appropriate method
   - Verify results match empirical observations

4. **Integration:** Connect to divide-and-conquer algorithms
   - Merge sort, Binary search, Strassen's multiplication
   - Understand why certain designs yield certain complexities

## Key Techniques Summary

| Technique | Best For | Complexity | Notes |
|---|---|---|---|
| Master Theorem | Quick analysis of T(n) = aT(n/b) + f(n) | O(1) application | Fastest; covers most cases |
| Substitution | Formal proofs, non-standard recurrences | Manual work | More tedious but rigorous |
| Iteration | Understanding recurrence behavior | Summation work | Great for intuition building |

## Master Theorem Cases

For T(n) = aT(n/b) + f(n), compare f(n) to n^(log_b a):

1. **f(n) = O(n^(log_b a - ε)):** T(n) = Θ(n^(log_b a))
2. **f(n) = Θ(n^(log_b a) log^k n):** T(n) = Θ(n^(log_b a) log^(k+1) n)
3. **f(n) = Ω(n^(log_b a + ε)):** T(n) = Θ(f(n)) if a·f(n/b) ≤ c·f(n)

## Key Takeaways

- Recurrence relations formally model recursive algorithm costs
- Master Theorem provides quick solution for divide-and-conquer patterns
- Three solution methods: Master (fastest), Substitution (rigorous), Iteration (intuitive)
- Understanding recurrences is essential for analyzing recursive algorithms
- Combine with earlier asymptotic notation knowledge to fully describe complexity
