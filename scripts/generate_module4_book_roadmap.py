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


def basic_notes(topic: str):
    return {
        "what": [
            f"`{topic}` is a core DSA topic from the roadmap.",
            "It focuses on pattern-based reasoning plus implementation discipline.",
        ],
        "core": [
            "Define state, transitions, invariants, and termination clearly.",
            "Use the right data structure for required operations.",
            "Validate with boundary cases and complexity analysis.",
        ],
        "why": [
            "Improves interview problem-solving speed and correctness.",
            "Builds transferable patterns for production engineering tasks.",
        ],
    }


def python_example(topic: str):
    t = topic.lower()
    if "linked list" in t:
        return """class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

head = Node(1, Node(2, Node(3)))
cur = head
while cur:
    print(cur.val, end=" ")
    cur = cur.next
print()
"""
    if "stack" in t:
        return """stack = []
stack.append(10)
stack.append(20)
print(stack.pop(), stack[-1])
"""
    if "queue" in t or "deque" in t:
        return """from collections import deque
q = deque([1, 2])
q.append(3)
print(q.popleft(), list(q))
"""
    if "hash" in t:
        return """freq = {}
for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
"""
    if "tree" in t or "bst" in t:
        return """class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v; self.l = l; self.r = r

root = Node(2, Node(1), Node(3))
def inorder(n):
    return inorder(n.l) + [n.v] + inorder(n.r) if n else []
print(inorder(root))
"""
    if "heap" in t or "top-k" in t:
        return """import heapq
nums = [5,1,9,2,7]
print(heapq.nsmallest(3, nums))
"""
    if "trie" in t or "prefix" in t:
        return """words = ["cat", "car", "dog"]
prefix = "ca"
print([w for w in words if w.startswith(prefix)])
"""
    if "binary search" in t or "search" in t:
        return """def bs(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target: return mid
        if nums[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
print(bs([1,3,5,7,9], 7))
"""
    if "sort" in t:
        return """nums = [5,2,8,1,3]
print(sorted(nums))
"""
    if "graph" in t or "bfs" in t or "dfs" in t:
        return """from collections import deque
g = {0:[1,2], 1:[3], 2:[3], 3:[]}
q = deque([0]); seen = {0}; order = []
while q:
    u = q.popleft(); order.append(u)
    for v in g[u]:
        if v not in seen:
            seen.add(v); q.append(v)
print(order)
"""
    if "dijkstra" in t or "shortest path" in t:
        return """import heapq
g = {0:[(1,4),(2,1)], 1:[(3,1)], 2:[(1,2),(3,5)], 3:[]}
dist = {0:0}
pq = [(0,0)]
while pq:
    d,u = heapq.heappop(pq)
    if d != dist.get(u, float('inf')): continue
    for v,w in g[u]:
        nd = d + w
        if nd < dist.get(v, float('inf')):
            dist[v] = nd
            heapq.heappush(pq, (nd, v))
print(dist)
"""
    if "union find" in t or "disjoint" in t:
        return """parent = list(range(6))
rank = [0]*6
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    ra, rb = find(a), find(b)
    if ra == rb: return
    if rank[ra] < rank[rb]: parent[ra] = rb
    elif rank[ra] > rank[rb]: parent[rb] = ra
    else: parent[rb] = ra; rank[ra] += 1
union(1,2); union(2,3)
print(find(1) == find(3))
"""
    if "segment tree" in t or "fenwick" in t or "bit" in t:
        return """nums = [1,2,3,4,5]
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
def range_sum(l, r):
    return prefix[r+1] - prefix[l]
print(range_sum(1,3))
"""
    if "dp" in t or "knapsack" in t or "lis" in t or "lcs" in t:
        return """def fib(n):
    dp = [0,1]
    for _ in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]
print(fib(10))
"""
    if "greedy" in t or "activity" in t or "scheduling" in t:
        return """intervals = [(1,3),(2,4),(3,5),(0,6),(5,7),(8,9)]
intervals.sort(key=lambda x: x[1])
count = 0
end = -10**9
for s,e in intervals:
    if s >= end:
        count += 1
        end = e
print(count)
"""
    if "bit" in t or "xor" in t:
        return """nums = [2,2,1,1,4]
x = 0
for n in nums:
    x ^= n
print(x)
"""
    if "cheat sheet" in t or "checklist" in t or "roadmap" in t:
        return """summary = {
    "Pattern": "Two Pointers",
    "When to use": "Sorted arrays / opposite-end decisions",
    "Pitfall": "Boundary and duplicate handling",
}
print(summary)
"""
    return """print("Build one runnable coding exercise for this topic.")\n"""


def java_snippet():
    return """```java
// Implement the same logic shown in Python.
// Keep method signatures clear and add edge-case tests.
```
"""


def build_notebook(day: int, topic: str, module_label: str, chapter_label: str):
    b = basic_notes(topic)
    py = python_example(topic)
    cells = [
        md(
            f"""
# Day {day:02d} - {topic}

**Module:** {module_label}  
**Chapter:** {chapter_label}
"""
        ),
        md(
            f"""
## Learning Objectives
- Understand **{topic}** through pattern-driven explanation.
- Implement a runnable Python solution and a Java equivalent.
- Validate with boundary tests and complexity analysis.
"""
        ),
        md(
            f"""
## Basic Notes
What is {topic}?
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
        ),
        md(
            """
## Python Example
Run and verify this example.
"""
        ),
        code(py),
        md(
            f"""
## Java Snippet
{java_snippet()}
"""
        ),
        md(
            f"""
## Mini Project
Implement a mini problem or utility around `{topic}`.

Deliverables:
- Clear problem statement
- Working implementation
- 3+ tests
- Time/space complexity
"""
        ),
        md(
            f"""
## Practice Problems
1. Explain `{topic}` in your own words.
2. Dry run one example by hand.
3. Implement Python and Java versions.
4. Add normal and edge test cases.
5. Write complexity and one optimization idea.
"""
        ),
        md(
            f"""
## Practice Solutions
1. **Definition / idea:** Start from state, constraints, and invariants for `{topic}`.
2. **Dry run answer:** Confirm transitions and stopping conditions on a small input.
3. **Implementation answer:** Use the Python solution cell and mirror the logic in Java.
4. **Platform problem answer:** Solve one related coding-platform problem and compare complexity.
5. **Common mistake + fix:** Mistake: coding before state design. Fix: write transitions first.
"""
        ),
        code(
            f"""# Practice Solution Code - Day {day:02d}: {topic}
{py}
print("Practice solution completed for: {topic}")
"""
        ),
        md(
            f"""
## Practice Solution Code (Java)
{java_snippet()}
"""
        ),
        md(
            """
## Blog Post Prompts
- Which pattern did you apply and why?
- Which edge case was most important?
- What complexity trade-off did you choose?
"""
        ),
        md(
            """
## Completion Checklist
- [ ] Concept understood
- [ ] Python solution run
- [ ] Java solution drafted/run
- [ ] 3+ tests added
- [ ] Complexity written
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


def build_readme(day: int, topic: str, notebook_name: str):
    b = basic_notes(topic)
    return textwrap.dedent(
        f"""
# Day {day:02d} - {topic}

Notebook: [{notebook_name}](./{notebook_name})

## Basic Notes

What is {topic}?
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
    base = root / "04-Book-DSA-Roadmap"
    base.mkdir(parents=True, exist_ok=True)

    module_label = "Book DSA Roadmap (Narasimha Karumanchi aligned)"
    start_day = 143

    chapters = [
        ("01-Linked-Lists", "Linked Lists", ["Singly Linked List", "Doubly Linked List", "Circular Linked List", "Fast & Slow Pointer", "Cycle Detection", "Linked List Reversal", "Merge Lists"]),
        ("02-Stacks", "Stacks", ["Stack Fundamentals", "Expression Evaluation", "Monotonic Stack", "Next Greater Element", "Histogram Problems"]),
        ("03-Queues", "Queues", ["Queue Fundamentals", "Circular Queue", "Deque", "Priority Queue", "Sliding Window Maximum"]),
        ("04-Hashing", "Hashing", ["Hash Tables", "Collision Resolution", "Open Addressing", "Chaining", "Frequency Maps"]),
        ("05-Trees", "Trees", ["Tree Fundamentals", "DFS Traversals", "BFS Traversals", "Tree Properties", "Tree Views", "Diameter Problems"]),
        ("06-Binary-Search-Trees", "Binary Search Trees", ["BST Operations", "Validation", "Successor & Predecessor", "Kth Smallest Element"]),
        ("07-Heaps", "Heaps", ["Min Heap", "Max Heap", "Heap Operations", "Heap Sort", "Top-K Problems"]),
        ("08-Tries", "Tries", ["Trie Fundamentals", "Prefix Search", "Auto Completion", "Dictionary Problems"]),
        ("09-Searching", "Searching", ["Linear Search", "Binary Search", "Variations of Binary Search"]),
        ("10-Sorting", "Sorting", ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Counting Sort", "Radix Sort"]),
        ("11-Divide-and-Conquer", "Divide and Conquer", ["Merge Sort", "Quick Sort", "Closest Pair", "Count Inversions", "Count Range Sum"]),
        ("12-Graph-Fundamentals", "Graph Fundamentals", ["Graph Representation", "Adjacency Matrix", "Adjacency List"]),
        ("13-Graph-Traversal", "Graph Traversal", ["BFS", "DFS", "Connected Components"]),
        ("14-Shortest-Path-Algorithms", "Shortest Path Algorithms", ["Dijkstra", "Bellman-Ford", "Floyd-Warshall"]),
        ("15-Minimum-Spanning-Tree", "Minimum Spanning Tree", ["Kruskal", "Prim", "Union Find"]),
        ("16-Advanced-Graph-Algorithms", "Advanced Graph Algorithms", ["Topological Sort", "SCC", "Articulation Points", "Bridges"]),
        ("17-Greedy-Algorithms", "Greedy Algorithms", ["Activity Selection", "Job Scheduling", "Huffman Coding"]),
        ("18-Dynamic-Programming", "Dynamic Programming", ["DP Fundamentals", "Memoization", "Tabulation", "1D DP", "2D DP", "Knapsack", "LIS", "LCS", "Matrix DP"]),
        ("19-Bit-Manipulation", "Bit Manipulation", ["Bit Operations", "XOR Tricks", "Bitmask DP"]),
        ("20-Disjoint-Set-Union", "Disjoint Set Union", ["Path Compression", "Union by Rank", "Applications"]),
        ("21-Segment-Trees", "Segment Trees", ["Range Queries", "Lazy Propagation"]),
        ("22-Fenwick-Tree", "Fenwick Tree", ["Prefix Queries", "Update Operations"]),
        ("23-Sparse-Table", "Sparse Table", ["Range Minimum Query"]),
        ("24-Advanced-Heaps", "Advanced Heaps", ["Indexed Heap", "Fibonacci Heap"]),
        ("25-Interview-Patterns-Arrays", "Interview Patterns - Arrays", ["Hashing", "Two Pointers", "Sliding Window", "Prefix Sum", "Binary Search"]),
        ("26-Interview-Patterns-Strings", "Interview Patterns - Strings", ["Hashing", "KMP", "Rabin-Karp", "Sliding Window"]),
        ("27-Interview-Patterns-Linked-List", "Interview Patterns - Linked List", ["Fast & Slow Pointer", "Reversal", "Merge"]),
        ("28-Interview-Patterns-Trees", "Interview Patterns - Trees", ["DFS", "BFS", "Tree DP", "LCA"]),
        ("29-Interview-Patterns-Graphs", "Interview Patterns - Graphs", ["BFS", "DFS", "Shortest Path", "Union Find"]),
        ("30-Interview-Patterns-DP", "Interview Patterns - Dynamic Programming", ["Knapsack", "Subsequence DP", "Grid DP", "State Machine DP"]),
        ("31-Interview-Patterns-Advanced", "Interview Patterns - Advanced", ["Monotonic Stack", "Monotonic Queue", "Sweep Line", "Divide & Conquer", "Meet in the Middle"]),
        ("32-Revision", "Revision", ["Complexity Cheat Sheet", "Pattern Cheat Sheet", "Interview Checklist", "Top 100 Interview Problems", "Top 200 LeetCode Mapping", "FAANG Interview Roadmap"]),
    ]

    all_topics = []
    day = start_day
    for folder, chapter_label, topic_list in chapters:
        chapter_dir = base / folder
        chapter_dir.mkdir(parents=True, exist_ok=True)
        for topic in topic_list:
            all_topics.append((day, folder, chapter_label, topic))
            day += 1

    for day_num, folder, chapter_label, topic in all_topics:
        chapter_dir = base / folder
        nb_name = f"{day_num:02d}-{slugify(topic)}.ipynb"
        nb_path = chapter_dir / nb_name
        nb = build_notebook(day_num, topic, module_label, chapter_label)
        nb_path.write_text(json.dumps(nb, indent=2), encoding="utf-8")

        readme_name = f"README-{day_num:02d}-{slugify(topic)}.md"
        (chapter_dir / readme_name).write_text(build_readme(day_num, topic, nb_name), encoding="utf-8")

    # chapter readmes
    for folder, chapter_label, _ in chapters:
        chapter_dir = base / folder
        notebooks = sorted(chapter_dir.glob("*.ipynb"))
        rows = []
        for nb in notebooks:
            day_part, topic_part = nb.stem.split("-", 1)
            topic_label = topic_part.replace("-", " ").title()
            topic_readme = f"README-{nb.stem}.md"
            rows.append(f"| {day_part} | {topic_label} | [{nb.name}](./{nb.name}) | [{topic_readme}](./{topic_readme}) |")
        content = "\n".join(
            [
                f"# {folder}",
                "",
                f"Chapter: {chapter_label}",
                "",
                "| Day | Topic | Notebook | Topic README |",
                "|---|---|---|---|",
                *rows,
            ]
        ) + "\n"
        (chapter_dir / "README.md").write_text(content, encoding="utf-8")

    # tracker
    tracker_rows = ["| Day | Topic | Status |", "|---|---|---|"]
    for day_num, _, _, topic in all_topics:
        tracker_rows.append(f"| {day_num:02d} | {topic} | [ ] |")
    tracker_md = "\n".join(
        [
            "# Book DSA Roadmap Tracker",
            "",
            "Track progress for book-aligned topics after core modules.",
            "",
            *tracker_rows,
        ]
    ) + "\n"

    guide_dir = base / "00-Program-Guide"
    guide_dir.mkdir(parents=True, exist_ok=True)
    tracker_nb = {
        "cells": [md(tracker_md)],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.13"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (guide_dir / "00-book-roadmap-tracker.ipynb").write_text(json.dumps(tracker_nb, indent=2), encoding="utf-8")
    (guide_dir / "README-00-book-roadmap-tracker.md").write_text(
        build_readme(0, "Book Roadmap Tracker", "00-book-roadmap-tracker.ipynb"),
        encoding="utf-8",
    )
    (guide_dir / "README.md").write_text(
        "# 00-Program-Guide\n\n| Day | Topic | Notebook | Topic README |\n|---|---|---|---|\n| 00 | Book Roadmap Tracker | [00-book-roadmap-tracker.ipynb](./00-book-roadmap-tracker.ipynb) | [README-00-book-roadmap-tracker.md](./README-00-book-roadmap-tracker.md) |\n",
        encoding="utf-8",
    )

    # module readme
    section_rows = ["| 00-Program-Guide | 1 | [Open](./00-Program-Guide/README.md) |"]
    for folder, _, topic_list in chapters:
        section_rows.append(f"| {folder} | {len(topic_list)} | [Open](./{folder}/README.md) |")
    module_readme = "\n".join(
        [
            "# Module 4: Book DSA Roadmap",
            "",
            "## Section Index",
            "| Section Folder | Notebook Count | Section README |",
            "|---|---:|---|",
            *section_rows,
        ]
    ) + "\n"
    (base / "README.md").write_text(module_readme, encoding="utf-8")

    print(f"Created module at: {base}")
    print(f"Topics created: {len(all_topics)}")
    print(f"Day range: {start_day}-{start_day + len(all_topics) - 1}")


if __name__ == "__main__":
    main()

