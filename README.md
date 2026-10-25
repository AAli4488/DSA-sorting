# LeetCode 23. Merge k Sorted Lists

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/

## Problem

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Example 1

```
Input:  lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

The linked-lists are:

```
1->4->5
1->3->4
2->6
```

Merging them into one sorted list: `1->1->2->3->4->4->5->6`

### Example 2

```
Input:  lists = []
Output: []
```

### Example 3

```
Input:  lists = [[]]
Output: []
```

### Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Approach: Min-Heap

1. Put the head of every non-empty list into a min-heap, so the smallest current value is always on top.
2. Pop the smallest node, attach it to the result list, then push that node's `next` node into the heap.
3. Repeat until the heap is empty.

The list index `i` in each heap tuple is a tie-breaker. When two values are equal, Python would otherwise try to compare `ListNode` objects and raise an error.

## Solution (Python)

```python
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Push the head of each non-empty list: (value, list index, node)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```

## Dry Run

Input: `[[1,4,5],[1,3,4],[2,6]]`

- Heap starts with the three heads: `1, 1, 2`.
- Pop `1`, push `4`. Pop `1`, push `3`. Pop `2`, push `6`.
- Continuing this way gives `[1,1,2,3,4,4,5,6]`.

## Complexity

| | Complexity | Notes |
|---|---|---|
| Time | `O(N log k)` | `N` = total number of nodes, `k` = number of lists |
| Space | `O(k)` | The heap holds at most one node per list |

## Alternative: Divide and Conquer

Merge the lists in pairs, then merge the results in pairs again, until one list remains. This has the same `O(N log k)` time and avoids the heap.

## Run Locally

The file `merge_k_sorted_lists.py` contains the solution with helper functions and test cases:

```
python merge_k_sorted_lists.py
```

---

# Sorting in DSA

Sorting is the process of arranging data (numbers, strings, records) in **ascending** or **descending** order. It is a foundational concept in Data Structures and Algorithms and underpins binary search, interval merging, scheduling, database indexing, and many algorithmic optimizations.

---

## Table of Contents

- [What Sorting Means](#what-sorting-means)
- [Categories of Sorting](#categories-of-sorting)
- [Internal vs External Sorting](#internal-vs-external-sorting)
- [Stability](#stability)
- [When to Use Which Algorithm](#when-to-use-which-algorithm)
- [Summary Table](#summary-table)
- [Code Example: Bubble Sort (Sort Colors)](#code-example-bubble-sort-sort-colors)
- [Code Example: Valid Parentheses (Stack)](#code-example-valid-parentheses-stack)
- [Conclusion](#conclusion)

---

## What Sorting Means

Sorting rearranges elements so they follow a logical sequence (e.g., smallest to largest). It is essential for:

- Binary search
- Interval merging
- Scheduling
- Database indexing
- Many algorithmic optimizations

---

## Categories of Sorting

### 1. Comparison-Based Sorting

These algorithms compare elements to determine their order.

| Algorithm | Time Complexity | Space | Notes |
|-----------|-----------------|-------|-------|
| Bubble Sort | O(n²) | O(1) | Simple, rarely used in practice |
| Selection Sort | O(n²) | O(1) | Fewer swaps |
| Insertion Sort | O(n²) | O(1) | Fast on small or nearly sorted data |
| Merge Sort | O(n log n) | O(n) | Stable |
| Quick Sort | O(n log n) avg, O(n²) worst | O(log n) | In-place, fast on average |
| Heap Sort | O(n log n) | O(1) | In-place |

### 2. Non-Comparison-Based Sorting

Used when the input range is known.

| Algorithm | Time Complexity | Notes |
|-----------|-----------------|-------|
| Counting Sort | O(n + k) | Best for small integer ranges |
| Radix Sort | O(nk) | Sorts digit by digit |
| Bucket Sort | O(n) average | Works well on uniformly distributed data |

---

## Internal vs External Sorting

- **Internal Sorting:** The entire dataset fits in RAM (Bubble, Insertion, Quick, Merge).
- **External Sorting:** Used when data is too large for memory (e.g., external Merge Sort).

---

## Stability

A **stable** algorithm preserves the relative order of equal elements.

- **Stable:** Merge Sort, Insertion Sort, Bubble Sort
- **Unstable:** Quick Sort, Heap Sort

---

## When to Use Which Algorithm

| Scenario | Best Algorithm | Reason |
|----------|----------------|--------|
| Small or nearly sorted data | Insertion Sort | Adaptive, fast for small inputs |
| Large random datasets | Quick Sort | Fast average-case performance |
| Worst-case guarantees | Merge Sort / Heap Sort | Always O(n log n) |
| Integers with limited range | Counting / Radix Sort | Linear time |

---

## Summary Table

| Algorithm | Time Complexity | Space | Stable | Type |
|-----------|-----------------|-------|--------|------|
| Bubble Sort | O(n²) | O(1) | Yes | Comparison |
| Selection Sort | O(n²) | O(1) | No | Comparison |
| Insertion Sort | O(n²) | O(1) | Yes | Comparison |
| Merge Sort | O(n log n) | O(n) | Yes | Comparison |
| Quick Sort | O(n log n) avg, O(n²) worst | O(log n) | No | Comparison |
| Heap Sort | O(n log n) | O(1) | No | Comparison |
| Counting Sort | O(n + k) | O(k) | Yes | Non-comparison |
| Radix Sort | O(nk) | O(n + k) | Yes | Non-comparison |

---

## Code Example: Bubble Sort (Sort Colors)

Bubble Sort with an early-exit optimization, applied to the LeetCode "Sort Colors" problem.

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n - 1):
            swapped = False

            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:  # already sorted, stop early
                break
```

**How it works:**

- Each pass compares adjacent elements and swaps them if they are out of order, pushing the largest remaining element to the end.
- The inner loop shrinks by `i` each pass because the last `i` elements are already in place.
- If a full pass makes no swaps, the array is sorted and the loop stops early.

**Complexity:** O(n²) worst/average time, O(n) best case (already sorted, thanks to the `swapped` flag), O(1) extra space.

> Note: Sort Colors can be solved in O(n) time with the Dutch National Flag algorithm or Counting Sort, which is what interviewers usually expect.

---

## Code Example: Valid Parentheses (Stack)

Checks whether a string of brackets `()[]{}` is balanced, using a stack (LeetCode "Valid Parentheses").

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs:  # closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:  # opening bracket
                stack.append(ch)

        return not stack  # valid only if nothing is left open
```

**How it works:**

- Opening brackets are pushed onto the stack.
- For each closing bracket, the top of the stack must be its matching opening bracket, otherwise the string is invalid.
- At the end, the stack must be empty, meaning every opening bracket was closed.

**Complexity:** O(n) time, O(n) space.

---

## Conclusion

Sorting is one of the most fundamental concepts in DSA and forms the basis of many advanced algorithms and interview problems. Choosing the right algorithm depends on data size, range, memory constraints, and whether stability matters.

## References

- [GeeksforGeeks – Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)
- [GUVI – Sorting Algorithms](https://www.guvi.in)
