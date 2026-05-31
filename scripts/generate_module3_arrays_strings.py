from pathlib import Path
import json
import re
import textwrap


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def src(text: str):
    return [line + "\n" for line in textwrap.dedent(text).strip("\n").splitlines()]


def md(text: str):
    return {"cell_type": "markdown", "metadata": {}, "source": src(text)}


def code(text: str):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": src(text),
    }


def basic_notes(title: str, kind: str):
    if kind == "problem":
        return {
            "what": [
                f"`{title}` is a pattern-oriented interview problem from arrays/strings/matrix tracks.",
                "A reliable solution starts with constraints, edge cases, and the best-fitting pattern.",
            ],
            "core": [
                "Define minimal state and valid transitions before implementation.",
                "Use deterministic pointer/index/window updates to avoid logic drift.",
                "Guard boundaries, duplicates, and termination conditions explicitly.",
            ],
            "why": [
                "Builds reusable problem-solving patterns for interviews and real systems.",
                "Improves coding speed and correctness under time pressure.",
            ],
        }

    topic_map = {
        "Introduction to Arrays": (
            [
                "Arrays store homogeneous elements in contiguous memory.",
                "They provide O(1) random access by index.",
            ],
            [
                "Address computation enables constant-time indexing.",
                "Middle insertion/deletion usually requires shifting elements.",
                "Array tasks often combine traversal with hashing/prefix/window patterns.",
            ],
        ),
        "Types of Arrays": (
            [
                "Arrays can be static/dynamic, 1D/2D, dense/sparse.",
                "Type choice affects memory usage and update/query cost.",
            ],
            [
                "Static arrays have fixed capacity; dynamic arrays resize with amortized cost.",
                "2D arrays can be flattened and indexed by row-major mapping.",
                "Sparse arrays should use compressed representations for memory efficiency.",
            ],
        ),
        "Advantages and Disadvantages of Arrays": (
            [
                "Arrays are simple, cache-friendly, and efficient for traversal.",
                "They are less flexible for frequent structural modifications.",
            ],
            [
                "Advantages: O(1) access and locality of reference.",
                "Disadvantages: costly middle insert/delete and occasional resize overhead.",
                "Use arrays when read/index operations dominate updates.",
            ],
        ),
        "Introduction to Strings": (
            [
                "Strings represent ordered character sequences used in parsing and matching.",
                "Most interview problems require careful indexing and character counting.",
            ],
            [
                "Immutability affects concatenation strategies and performance.",
                "ASCII/Unicode assumptions can change correctness for edge cases.",
                "Common techniques include two-pointers, windows, and frequency maps.",
            ],
        ),
        "String Manipulation": (
            [
                "String manipulation transforms text while preserving rule constraints.",
                "Correct boundaries and normalization decisions are critical.",
            ],
            [
                "Off-by-one and empty-input bugs are common failure points.",
                "Prefer linear scans and hash-based counts where possible.",
                "Document assumptions about casing, punctuation, and encoding.",
            ],
        ),
        "String Matching Algorithms": (
            [
                "String matching locates pattern occurrences inside larger text.",
                "Algorithm choice depends on input size and preprocessing budget.",
            ],
            [
                "Naive matching is simple but can degrade to O(n*m).",
                "KMP uses prefix-function preprocessing for linear matching.",
                "Rabin-Karp uses rolling hashes with collision verification.",
            ],
        ),
        "Introduction to 2D Arrays": (
            [
                "2D arrays model grid-like data with row/column coordinates.",
                "Matrix problems emphasize traversal order and boundaries.",
            ],
            [
                "Coordinate consistency prevents indexing bugs.",
                "Neighborhood rules (4-dir/8-dir) change traversal behavior.",
                "Many tasks combine simulation, marking, and constraint checks.",
            ],
        ),
        "Types of 2D Arrays": (
            [
                "2D arrays can be square/rectangular, dense/sparse, static/dynamic.",
                "Storage layout should align with query/update workloads.",
            ],
            [
                "Square matrices support in-place transforms like rotation.",
                "Rectangular matrices require strict row/column bound handling.",
                "Sparse matrices benefit from compressed coordinate structures.",
            ],
        ),
        "Advantages and Disadvantages of 2D Arrays": (
            [
                "2D arrays naturally represent grids and DP state tables.",
                "They can become memory-heavy on large dimensions.",
            ],
            [
                "Advantages: intuitive modeling and direct coordinate access.",
                "Disadvantages: high memory footprint and potential cache inefficiency.",
                "Use locality-aware traversal for better practical performance.",
            ],
        ),
    }

    what, core = topic_map.get(
        title,
        (
            [
                f"`{title}` is a foundational arrays/strings concept.",
                "The key is mapping theory to concrete coding patterns and edge checks.",
            ],
            [
                "Define state and transitions explicitly.",
                "Validate edge cases before micro-optimizing.",
                "Capture time and space complexity with assumptions.",
            ],
        ),
    )

    return {
        "what": what,
        "core": core,
        "why": [
            "Improves pattern recognition and implementation confidence.",
            "Bridges theory with practical interview-quality coding.",
        ],
    }


SOLUTIONS = {
    "Two Sum": """def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
""",
    "Best Time to Buy and Sell Stock": """def max_profit(prices):
    min_price = float('inf')
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best

print(max_profit([7, 1, 5, 3, 6, 4]))
""",
    "Contains Duplicate": """def contains_duplicate(nums):
    return len(nums) != len(set(nums))

print(contains_duplicate([1, 2, 3, 1]))
""",
    "Product of Array Except Self": """def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    pref = 1
    for i in range(n):
        out[i] = pref
        pref *= nums[i]
    suff = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suff
        suff *= nums[i]
    return out

print(product_except_self([1, 2, 3, 4]))
""",
    "Maximum Subarray": """def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
""",
    "Maximum Product Subarray": """def max_product(nums):
    cur_max = cur_min = ans = nums[0]
    for x in nums[1:]:
        a, b = cur_max * x, cur_min * x
        cur_max = max(x, a, b)
        cur_min = min(x, a, b)
        ans = max(ans, cur_max)
    return ans

print(max_product([2,3,-2,4]))
""",
    "Find Minimum in Rotated Sorted Array": """def find_min(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

print(find_min([4,5,6,7,0,1,2]))
""",
    "Search in Rotated Sorted Array": """def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print(search([4,5,6,7,0,1,2], 0))
""",
    "3Sum": """def three_sum(nums):
    nums.sort()
    out = []
    for i in range(len(nums)):
        if i and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                out.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return out

print(three_sum([-1,0,1,2,-1,-4]))
""",
    "3Sum Closest": """def three_sum_closest(nums, target):
    nums.sort()
    best = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(best - target):
                best = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return s
    return best

print(three_sum_closest([-1,2,1,-4], 1))
""",
    "4Sum": """def four_sum(nums, target):
    nums.sort()
    out = []
    n = len(nums)
    for i in range(n - 3):
        if i and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l, r = j + 1, n - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    out.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return out

print(four_sum([1,0,-1,0,-2,2], 0))
""",
    "4Sum II": """from collections import Counter

def four_sum_count(a, b, c, d):
    ab = Counter(x + y for x in a for y in b)
    return sum(ab[-(x + y)] for x in c for y in d)

print(four_sum_count([1,2],[-2,-1],[-1,2],[0,2]))
""",
    "Valid Anagram": """from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

print(is_anagram("anagram", "nagaram"))
""",
    "Valid Palindrome": """def is_palindrome(s):
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
""",
    "Longest Common Prefix": """def longest_common_prefix(strs):
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(["flower","flow","flight"]))
""",
    "Longest Substring Without Repeating Characters": """def length_of_longest_substring(s):
    left = 0
    seen = {}
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best

print(length_of_longest_substring("abcabcbb"))
""",
    "Longest Repeating Character Replacement": """from collections import defaultdict

def character_replacement(s, k):
    count = defaultdict(int)
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        max_freq = max(max_freq, count[ch])
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

print(character_replacement("AABABBA", 1))
""",
    "Minimum Window Substring": """from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

print(min_window("ADOBECODEBANC", "ABC"))
""",
    "Group Anagrams": """from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
""",
    "Set Matrix Zeroes": """def set_zeroes(matrix):
    rows, cols = set(), set()
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                rows.add(r); cols.add(c)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in rows or c in cols:
                matrix[r][c] = 0
    return matrix

print(set_zeroes([[1,1,1],[1,0,1],[1,1,1]]))
""",
    "Spiral Matrix": """def spiral_order(matrix):
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
    return res

print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
""",
    "Rotate Image": """def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
""",
    "Word Search": """def exist(board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
        tmp = board[r][c]
        board[r][c] = '#'
        found = (
            dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1)
        )
        board[r][c] = tmp
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
""",
    "Pascal's Triangle": """def generate(num_rows):
    out = []
    for r in range(num_rows):
        row = [1] * (r + 1)
        for c in range(1, r):
            row[c] = out[r - 1][c - 1] + out[r - 1][c]
        out.append(row)
    return out

print(generate(5))
""",
    "Pascal's Triangle II": """def get_row(row_index):
    row = [1]
    for _ in range(row_index):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row

print(get_row(3))
""",
    "Unique Paths": """def unique_paths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c - 1]
    return dp[-1]

print(unique_paths(3, 7))
""",
    "Unique Paths II": """def unique_paths_with_obstacles(grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1 if grid[0][0] == 0 else 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]

print(unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]))
""",
    "Minimum Path Sum": """def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0:
                dp[c] = grid[r][c]
            elif r == 0:
                dp[c] = dp[c - 1] + grid[r][c]
            elif c == 0:
                dp[c] = dp[c] + grid[r][c]
            else:
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
    return dp[-1]

print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))
""",
    "Dungeon Game": """def calculate_minimum_hp(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    INF = 10**9
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    dp[m][n - 1] = dp[m - 1][n] = 1
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            need = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
            dp[r][c] = 1 if need <= 0 else need
    return dp[0][0]

print(calculate_minimum_hp([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
""",
    "Maximal Square": """def maximal_square(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best = 0
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if matrix[r - 1][c - 1] in ("1", 1):
                dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                best = max(best, dp[r][c])
    return best * best

print(maximal_square([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
""",
    "Maximal Rectangle": """def maximal_rectangle(matrix):
    if not matrix:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    best = 0

    def largest_histogram(h):
        stack = []
        ans = 0
        for i, x in enumerate(h + [0]):
            while stack and h[stack[-1]] > x:
                H = h[stack.pop()]
                L = stack[-1] if stack else -1
                ans = max(ans, H * (i - L - 1))
            stack.append(i)
        return ans

    for row in matrix:
        for c in range(n):
            heights[c] = heights[c] + 1 if row[c] in ("1", 1) else 0
        best = max(best, largest_histogram(heights))
    return best

print(maximal_rectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
""",
    "Count of Smaller Numbers After Self": """def count_smaller(nums):
    arr = list(enumerate(nums))
    counts = [0] * len(nums)

    def sort(lo, hi):
        if hi - lo <= 1:
            return arr[lo:hi]
        mid = (lo + hi) // 2
        left = sort(lo, mid)
        right = sort(mid, hi)
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                counts[left[i][0]] += j
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        while i < len(left):
            counts[left[i][0]] += j
            merged.append(left[i]); i += 1
        while j < len(right):
            merged.append(right[j]); j += 1
        arr[lo:hi] = merged
        return merged

    sort(0, len(nums))
    return counts

print(count_smaller([5,2,6,1]))
""",
}


def concept_python_example(title: str):
    examples = {
        "Introduction to Arrays": "nums = [10, 20, 30, 40]\nprint(nums[2])\n",
        "Types of Arrays": "one_d = [1, 2, 3]\ntwo_d = [[1, 2], [3, 4]]\nprint(one_d, two_d)\n",
        "Advantages and Disadvantages of Arrays": "nums = [1, 2, 3, 4]\nnums.insert(2, 99)\nprint(nums)\n",
        "Introduction to Strings": "s = 'algorithm'\nprint(s[0], s[-1], len(s))\n",
        "String Manipulation": "s = 'dsa'\nprint(s.upper(), s[::-1])\n",
        "String Matching Algorithms": "text = 'abracadabra'\npattern = 'cada'\nprint(text.find(pattern))\n",
        "Introduction to 2D Arrays": "grid = [[1,2,3],[4,5,6]]\nprint(grid[1][2])\n",
        "Types of 2D Arrays": "rect = [[1,2,3],[4,5,6]]\nsquare = [[1,2],[3,4]]\nprint(len(rect), len(square))\n",
        "Advantages and Disadvantages of 2D Arrays": "grid = [[0] * 3 for _ in range(3)]\ngrid[1][1] = 1\nprint(grid)\n",
    }
    return examples.get(title, "print('Add topic demo')\n")


def java_snippet(kind: str):
    if kind == "problem":
        return """```java
// Implement the same logic shown in Python for this problem.
// Keep method signature interview-friendly and add edge-case tests.
```
"""
    return """```java
public class Demo {
    public static void main(String[] args) {
        System.out.println("Run concept demo in Java");
    }
}
```
"""


def build_basic_notes_md(title: str, kind: str):
    b = basic_notes(title, kind)
    return f"""
## Basic Notes
What is {title}?
- {b['what'][0]}
- {b['what'][1]}

Core theory details:
- {b['core'][0]}
- {b['core'][1]}
- {b['core'][2]}

Why this matters for hands-on coding:
- {b['why'][0]}
- {b['why'][1]}
"""


def build_notebook(day: int, title: str, section_label: str, kind: str):
    py_code = SOLUTIONS.get(title, concept_python_example(title))
    cells = [
        md(
            f"""
# Day {day:02d} - {title}

**Module:** Arrays and Strings  
**Section:** {section_label}
"""
        ),
        md(
            f"""
## Learning Objectives
- Understand **{title}** using practical coding patterns.
- Implement a clean Python solution and a Java equivalent.
- Validate correctness with edge cases and complexity analysis.
"""
        ),
        md(build_basic_notes_md(title, kind)),
        md(
            """
## Python Example
Run and verify this example.
"""
        ),
        code(py_code),
        md(
            f"""
## Java Snippet
{java_snippet(kind)}
"""
        ),
        md(
            f"""
## Mini Project
Build a mini implementation around `{title}` with test coverage and complexity notes.

Deliverables:
- Problem statement
- Approach + trade-offs
- Test cases
- Complexity summary
"""
        ),
        md(
            f"""
## Practice Problems
1. Explain `{title}` in your own words.
2. Perform one manual dry run.
3. Implement in Python and Java.
4. Add 3+ test cases.
5. Write time/space complexity and one optimization idea.
"""
        ),
        md(
            f"""
## Practice Solutions
1. **Definition / idea:** `{title}` should start from pattern selection and constraints.
2. **Dry run answer:** Validate one standard case and one edge case before full implementation.
3. **Implementation answer:** Use the Python reference cell and mirror logic in Java.
4. **Platform problem answer:** Solve `{title}` with complexity write-up.
5. **Common mistake + fix:** Mistake: coding without invariant. Fix: define state/transition first.
"""
        ),
        code(
            f"""# Practice Solution Code - Day {day:02d}: {title}
{py_code}
print("Practice solution completed for: {title}")
"""
        ),
        md(
            f"""
## Practice Solution Code (Java)
{java_snippet(kind)}
"""
        ),
        md(
            """
## Blog Post Prompts
- What pattern did you use and why?
- Which edge case changed your implementation?
- What is the complexity and can it be improved?
"""
        ),
        md(
            """
## Completion Checklist
- [ ] Concept understood
- [ ] Python solution run
- [ ] Java solution drafted/run
- [ ] Test cases added
- [ ] Complexity documented
- [ ] GitHub + blog update completed
"""
        ),
    ]

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.13"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def build_topic_readme(day: int, title: str, notebook_name: str, kind: str):
    b = basic_notes(title, kind)
    return textwrap.dedent(
        f"""
# Day {day:02d} - {title}

Notebook: [{notebook_name}](./{notebook_name})

## Basic Notes

What is {title}?
- {b['what'][0]}
- {b['what'][1]}

Core theory details:
- {b['core'][0]}
- {b['core'][1]}
- {b['core'][2]}

Why this matters for hands-on coding:
- {b['why'][0]}
- {b['why'][1]}

## Hands-on Coding
1. Run the Python example and verify output.
2. Implement or refine the Java solution for the same logic.
3. Add at least 3 test cases (normal, edge, invalid/boundary).
4. Write time and space complexity.
5. Commit changes and add a short learning note.
"""
    ).strip() + "\n"


def main():
    root = Path.cwd()
    base = root / "03-Arrays-and-Strings"

    sections = {
        "00-Program-Guide": "Program Guide",
        "01-Arrays-Foundations": "Arrays Foundations",
        "02-Arrays-Practice-Problems": "Arrays Practice Problems",
        "03-Strings-Foundations": "Strings Foundations",
        "04-Strings-Practice-Problems": "Strings Practice Problems",
        "05-2D-Arrays-Foundations": "2D Arrays Foundations",
        "06-2D-Arrays-Practice-Problems": "2D Arrays Practice Problems",
        "templates": "Templates",
    }

    for folder in sections:
        (base / folder).mkdir(parents=True, exist_ok=True)

    arrays_foundations = [
        "Introduction to Arrays",
        "Types of Arrays",
        "Advantages and Disadvantages of Arrays",
    ]
    arrays_problems = [
        "Two Sum",
        "Best Time to Buy and Sell Stock",
        "Contains Duplicate",
        "Product of Array Except Self",
        "Maximum Subarray",
        "Maximum Product Subarray",
        "Find Minimum in Rotated Sorted Array",
        "Search in Rotated Sorted Array",
        "3Sum",
        "3Sum Closest",
        "4Sum",
        "4Sum II",
        "Valid Anagram",
        "Valid Palindrome",
        "Longest Common Prefix",
        "Longest Substring Without Repeating Characters",
        "Longest Repeating Character Replacement",
        "Minimum Window Substring",
        "Group Anagrams",
    ]
    strings_foundations = [
        "Introduction to Strings",
        "String Manipulation",
        "String Matching Algorithms",
    ]
    strings_problems = [
        "Valid Anagram",
        "Valid Palindrome",
        "Longest Common Prefix",
        "Longest Substring Without Repeating Characters",
        "Longest Repeating Character Replacement",
        "Minimum Window Substring",
        "Group Anagrams",
    ]
    matrix_foundations = [
        "Introduction to 2D Arrays",
        "Types of 2D Arrays",
        "Advantages and Disadvantages of 2D Arrays",
    ]
    matrix_problems = [
        "Set Matrix Zeroes",
        "Spiral Matrix",
        "Rotate Image",
        "Word Search",
        "Pascal's Triangle",
        "Pascal's Triangle II",
        "Unique Paths",
        "Unique Paths II",
        "Minimum Path Sum",
        "Dungeon Game",
        "Maximal Square",
        "Maximal Rectangle",
        "Count of Smaller Numbers After Self",
    ]

    topics = []
    day = 95
    for t in arrays_foundations:
        topics.append((day, "01-Arrays-Foundations", sections["01-Arrays-Foundations"], t, "concept"))
        day += 1
    for t in arrays_problems:
        topics.append((day, "02-Arrays-Practice-Problems", sections["02-Arrays-Practice-Problems"], t, "problem"))
        day += 1
    for t in strings_foundations:
        topics.append((day, "03-Strings-Foundations", sections["03-Strings-Foundations"], t, "concept"))
        day += 1
    for t in strings_problems:
        topics.append((day, "04-Strings-Practice-Problems", sections["04-Strings-Practice-Problems"], t, "problem"))
        day += 1
    for t in matrix_foundations:
        topics.append((day, "05-2D-Arrays-Foundations", sections["05-2D-Arrays-Foundations"], t, "concept"))
        day += 1
    for t in matrix_problems:
        topics.append((day, "06-2D-Arrays-Practice-Problems", sections["06-2D-Arrays-Practice-Problems"], t, "problem"))
        day += 1

    for day_num, folder, section_label, title, kind in topics:
        slug = slugify(title)
        notebook_name = f"{day_num:02d}-{slug}.ipynb"
        notebook_path = base / folder / notebook_name
        notebook_path.write_text(json.dumps(build_notebook(day_num, title, section_label, kind), indent=2), encoding="utf-8")

        readme_name = f"README-{day_num:02d}-{slug}.md"
        (base / folder / readme_name).write_text(build_topic_readme(day_num, title, notebook_name, kind), encoding="utf-8")

    # section readmes
    for folder, label in sections.items():
        folder_path = base / folder
        notebooks = sorted(folder_path.glob("*.ipynb"))
        if not notebooks:
            (folder_path / "README.md").write_text(f"# {folder}\n\nSupport files for {label}.\n", encoding="utf-8")
            continue
        rows = []
        for nb in notebooks:
            readme_name = f"README-{nb.stem}.md"
            day_part, topic_part = nb.stem.split("-", 1)
            topic_label = topic_part.replace("-", " ").title()
            rows.append(f"| {day_part} | {topic_label} | [{nb.name}](./{nb.name}) | [{readme_name}](./{readme_name}) |")
        content = "\n".join(
            [
                f"# {folder}",
                "",
                f"Section: {label}",
                "",
                "| Day | Topic | Notebook | Topic README |",
                "|---|---|---|---|",
                *rows,
            ]
        ) + "\n"
        (folder_path / "README.md").write_text(content, encoding="utf-8")

    tracker_rows = ["| Day | Topic | Status |", "|---|---|---|"]
    for day_num, _, _, title, _ in topics:
        tracker_rows.append(f"| {day_num:02d} | {title} | [ ] |")
    tracker_md = "\n".join(
        [
            "# Arrays and Strings Tracker",
            "",
            "Module covers Days 95 onward for Arrays, Strings, and 2D Arrays.",
            "",
            *tracker_rows,
        ]
    ) + "\n"

    tracker_nb = {
        "cells": [md(tracker_md)],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.13"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (base / "00-Program-Guide" / "00-arrays-strings-tracker.ipynb").write_text(json.dumps(tracker_nb, indent=2), encoding="utf-8")
    (base / "00-Program-Guide" / "README-00-arrays-strings-tracker.md").write_text(
        textwrap.dedent(
            """
            # Day 00 - Arrays and Strings Tracker

            Notebook: [00-arrays-strings-tracker.ipynb](./00-arrays-strings-tracker.ipynb)

            ## Basic Notes

            What is Arrays and Strings Tracker?
            - This tracker helps you monitor daily execution and consistency.
            - It keeps challenge momentum visible through completed checkboxes.

            Core theory details:
            - Consistency beats intensity in DSA growth.
            - Track solved patterns, not just solved problem counts.
            - Revisit weak topics after periodic review cycles.

            Why this matters for hands-on coding:
            - Better tracking exposes weak patterns early.
            - Structured review improves retention and interview readiness.

            ## Hands-on Coding
            1. Mark daily completion.
            2. Add one learning note per day.
            3. Revisit unsolved items weekly.
            4. Track complexity quality, not just acceptance.
            5. Keep momentum by shipping daily.
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )
    (base / "00-Program-Guide" / "README.md").write_text(
        "# 00-Program-Guide\n\n| Day | Topic | Notebook | Topic README |\n|---|---|---|---|\n| 00 | Arrays Strings Tracker | [00-arrays-strings-tracker.ipynb](./00-arrays-strings-tracker.ipynb) | [README-00-arrays-strings-tracker.md](./README-00-arrays-strings-tracker.md) |\n",
        encoding="utf-8",
    )

    (base / "templates" / "daily-problem-template.md").write_text(
        "# Daily Problem Template\n\n## Problem\n## Approach\n## Complexity\n## Python\n## Java\n## Tests\n## Learnings\n",
        encoding="utf-8",
    )
    (base / "templates" / "README.md").write_text("# templates\n\nTemplate files for this module.\n", encoding="utf-8")

    # module readme
    section_order = [
        "00-Program-Guide",
        "01-Arrays-Foundations",
        "02-Arrays-Practice-Problems",
        "03-Strings-Foundations",
        "04-Strings-Practice-Problems",
        "05-2D-Arrays-Foundations",
        "06-2D-Arrays-Practice-Problems",
        "templates",
    ]
    rows = []
    for folder in section_order:
        nb_count = len(list((base / folder).glob("*.ipynb")))
        rows.append(f"| {folder} | {nb_count} | [Open](./{folder}/README.md) |")
    module_readme = "\n".join(
        [
            "# Module 3: Arrays and Strings",
            "",
            "## Section Index",
            "| Section Folder | Notebook Count | Section README |",
            "|---|---:|---|",
            *rows,
        ]
    ) + "\n"
    (base / "README.md").write_text(module_readme, encoding="utf-8")

    print(f"Created module at: {base}")
    print(f"Topics created: {len(topics)}")
    print(f"Day range: 95-{95 + len(topics) - 1}")


if __name__ == "__main__":
    main()

