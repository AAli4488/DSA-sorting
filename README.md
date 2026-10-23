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

## Conclusion

Sorting is one of the most fundamental concepts in DSA and forms the basis of many advanced algorithms and interview problems. Choosing the right algorithm depends on data size, range, memory constraints, and whether stability matters.

---

## References

- [GeeksforGeeks – Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)
- [GUVI – Sorting Algorithms](https://www.guvi.in)
