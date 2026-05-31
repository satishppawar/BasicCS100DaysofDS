"""
Combined code for Basics (Days 01-06):
- Basics
- Variables (System-defined vs User-defined)
- Data Types
- Data Structure
- Abstract Data Type (ADT)
- Algorithms
"""

from collections import deque


def demo_basics():
    """Day 01: Basics demo."""
    a = 10
    b = 20
    sum_value = a + b
    is_large = sum_value > 25
    result = {"a": a, "b": b, "sum": sum_value, "is_large": is_large}
    print("Day 01:", result)
    return result


class UserDefined:
    """Day 02: User-defined type example."""

    def __init__(self, name):
        self.name = name


def demo_variables_system_vs_user():
    """Day 02: System-defined vs user-defined variables."""
    system_defined = 42
    user_defined = UserDefined("node")
    result = (type(system_defined).__name__, type(user_defined).__name__, user_defined.name)
    print("Day 02:", result)
    return result


def demo_data_types():
    """Day 03: Data types demo."""
    items = [1, 2, 2, 3]
    unique_items = set(items)
    lookup = {"a": 1, "b": 2}
    result = (len(items), len(unique_items), lookup["a"])
    print("Day 03:", result)
    return result


def demo_data_structure_stack():
    """Day 04: Stack behavior with list."""
    stack = []
    stack.append(10)
    stack.append(20)
    top_before_pop = stack[-1]
    popped = stack.pop()
    result = (top_before_pop, popped, len(stack))
    print("Day 04:", result)
    return result


def demo_adt_queue():
    """Day 05: Queue ADT behavior with deque."""
    queue = deque()
    queue.append("task-1")
    queue.append("task-2")
    first = queue.popleft()
    result = (first, list(queue))
    print("Day 05:", result)
    return result


def linear_search(nums, target):
    """Day 06: Linear search algorithm.

    Time: O(n)
    Space: O(1)
    """
    for i, value in enumerate(nums):
        if value == target:
            return i
    return -1


def demo_algorithms():
    """Day 06: Algorithm demo."""
    nums = [4, 8, 15, 16, 23, 42]
    found = linear_search(nums, 23)
    not_found = linear_search(nums, 99)
    result = (found, not_found)
    print("Day 06:", result)
    return result


def run_tests():
    """Basic correctness checks."""
    r1 = demo_basics()
    assert r1["sum"] == 30
    assert r1["is_large"] is True

    r2 = demo_variables_system_vs_user()
    assert r2[0] == "int"
    assert r2[1] == "UserDefined"
    assert r2[2] == "node"

    r3 = demo_data_types()
    assert r3 == (4, 3, 1)

    r4 = demo_data_structure_stack()
    assert r4 == (20, 20, 1)

    r5 = demo_adt_queue()
    assert r5 == ("task-1", ["task-2"])

    r6 = demo_algorithms()
    assert r6 == (4, -1)

    print("All combined basics tests passed.")


if __name__ == "__main__":
    run_tests()
