# 02-Algorithm-Analysis-and-Growth

**Notebook:** [02-algorithm-analysis-combined-all-days.ipynb](./02-algorithm-analysis-combined-all-days.ipynb)

This folder covers the fundamental principles of analyzing algorithm efficiency and understanding how algorithms perform as input size grows.

## Module Overview

This section teaches you how to analyze and compare algorithms based on their efficiency characteristics. You'll learn to measure algorithmic performance independent of hardware constraints and predict scalability before deployment.

## Core Concepts

### What is Algorithm Analysis?
Algorithm analysis describes how runtime and memory usage grow with input size `n`. Through asymptotic analysis, we compare algorithm behavior independent of hardware constants to make sound design decisions.

**Key principles:**
- Analysis predicts scalability before deployment
- Hardware speedups cannot fix bad asymptotic growth
- Use analysis to choose among multiple correct solutions
- Asymptotic analysis compares algorithms independent of machine and language

### Why Analyze Algorithms?
- **Estimate resource usage** as input size grows
- **Compare algorithms** independent of specific machines/languages
- **Focus on dominant growth terms** that matter for large inputs
- **Identify bottlenecks** and optimization opportunities

### How to Compare Algorithms
Effective algorithm comparison requires:
- Comparing time, space, and implementation complexity
- Using the same input model and constraints for fairness
- Preferring predictable performance for production workloads
- Understanding growth rates to make fast design decisions

## Core Theory Details

### Growth Rate Analysis
- **Growth rate** shows how cost scales with input size `n`
- Lower-order terms matter less for large `n`
- Use growth classes to make fast design decisions

### Common Growth Functions (in order)
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

### Specific Complexity Classes

**Constant Time - O(1):**
- Does not grow with input size
- Array index access and hash lookup examples
- Worst-case hash behavior can differ from average-case

**Logarithmic Time - O(log n):**
- Appears when problem size shrinks by a factor
- Binary search is the canonical example
- Requires ordered structure or divide strategy

**Linear Time - O(n):**
- One pass proportional to input size
- Best baseline for scan/filter/aggregate tasks
- Check if multiple passes can be merged into one

**Log-Linear Time - O(n log n):**
- Typical for efficient comparison sorting
- Divide-and-conquer often yields this complexity
- Good tradeoff for large general-purpose inputs

**Quadratic Time - O(n²):**
- Often comes from nested loops over same input
- Works for small `n` but degrades quickly
- Look for hashing/sorting/two-pointer optimizations

**Sub-linear Time:**
- Processing less than all elements
- Usually relies on indexing, ordering, or sampling
- Cannot fully validate every element-level constraint

**Super-linear Time:**
- Grows faster than O(n)
- O(n log n) is often acceptable; O(n²) can be costly
- Analyze upper input bounds before selecting approach

**Exponential Time - O(2ⁿ):**
- Usually means brute-force choice exploration
- Common in naive recursion/backtracking
- Pruning, memoization, and DP can reduce growth

**Factorial Time - O(n!):**
- Appears in permutation/ordering problems
- Search space explodes extremely fast
- Use constraints/pruning to make solutions practical

**Polynomial Time - O(n^k):**
- Generally tractable compared to exponential classes
- Lower-degree polynomials scale much better

## Hands-on Coding

For each topic:
1. Run the Python example and verify output
2. Implement or refine the Java solution for the same logic
3. Add at least 3 test cases (normal, edge, invalid/boundary)
4. Write time and space complexity analysis
5. Commit changes and add a short learning note

## Included Topics
| Day | Topic | Notebook | Topic README |
|---|---|---|---|
| 07 | Why Analysis of Algorithms | [07-why-analysis-of-algorithms.ipynb](./07-why-analysis-of-algorithms.ipynb) | [README-07-why-analysis-of-algorithms.md](./README-07-why-analysis-of-algorithms.md) |
| 08 | Goal of Analysis of Algorithms | [08-goal-of-analysis-of-algorithms.ipynb](./08-goal-of-analysis-of-algorithms.ipynb) | [README-08-goal-of-analysis-of-algorithms.md](./README-08-goal-of-analysis-of-algorithms.md) |
| 09 | Running Time Analysis | [09-running-time-analysis.ipynb](./09-running-time-analysis.ipynb) | [README-09-running-time-analysis.md](./README-09-running-time-analysis.md) |
| 10 | How to Compare Algorithms | [10-how-to-compare-algorithms.ipynb](./10-how-to-compare-algorithms.ipynb) | [README-10-how-to-compare-algorithms.md](./README-10-how-to-compare-algorithms.md) |
| 11 | Rate of Growth | [11-rate-of-growth.ipynb](./11-rate-of-growth.ipynb) | [README-11-rate-of-growth.md](./README-11-rate-of-growth.md) |
| 12 | Commonly Used Growth Functions | [12-commonly-used-growth-functions.ipynb](./12-commonly-used-growth-functions.ipynb) | [README-12-commonly-used-growth-functions.md](./README-12-commonly-used-growth-functions.md) |
| 13 | Logarithmic Time Complexity | [13-logarithmic-time-complexity.ipynb](./13-logarithmic-time-complexity.ipynb) | [README-13-logarithmic-time-complexity.md](./README-13-logarithmic-time-complexity.md) |
| 14 | Linear Time Complexity | [14-linear-time-complexity.ipynb](./14-linear-time-complexity.ipynb) | [README-14-linear-time-complexity.md](./README-14-linear-time-complexity.md) |
| 15 | Quadratic Time Complexity | [15-quadratic-time-complexity.ipynb](./15-quadratic-time-complexity.ipynb) | [README-15-quadratic-time-complexity.md](./README-15-quadratic-time-complexity.md) |
| 16 | Exponential Time Complexity | [16-exponential-time-complexity.ipynb](./16-exponential-time-complexity.ipynb) | [README-16-exponential-time-complexity.md](./README-16-exponential-time-complexity.md) |
| 17 | Factorial Time Complexity | [17-factorial-time-complexity.ipynb](./17-factorial-time-complexity.ipynb) | [README-17-factorial-time-complexity.md](./README-17-factorial-time-complexity.md) |
| 18 | Constant Time Complexity | [18-constant-time-complexity.ipynb](./18-constant-time-complexity.ipynb) | [README-18-constant-time-complexity.md](./README-18-constant-time-complexity.md) |
| 19 | Log Linear Time Complexity | [19-log-linear-time-complexity.ipynb](./19-log-linear-time-complexity.ipynb) | [README-19-log-linear-time-complexity.md](./README-19-log-linear-time-complexity.md) |
| 20 | Sub-linear Time Complexity | [20-sub-linear-time-complexity.ipynb](./20-sub-linear-time-complexity.ipynb) | [README-20-sub-linear-time-complexity.md](./README-20-sub-linear-time-complexity.md) |
| 21 | Super-linear Time Complexity | [21-super-linear-time-complexity.ipynb](./21-super-linear-time-complexity.ipynb) | [README-21-super-linear-time-complexity.md](./README-21-super-linear-time-complexity.md) |
| 22 | Polynomial Time Complexity | [22-polynomial-time-complexity.ipynb](./22-polynomial-time-complexity.ipynb) | [README-22-polynomial-time-complexity.md](./README-22-polynomial-time-complexity.md) |

## Key Takeaways

- Algorithm analysis measures efficiency independent of hardware
- Growth functions classify algorithms into standard complexity classes
- Know the ordering: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
- Choose algorithms based on expected input size and constraints
- Always pair time complexity analysis with space complexity
