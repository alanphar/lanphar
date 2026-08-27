"""The Problem: Merge Intervals.

Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3], [2,6], [8,10], [15,18]]

Output: [[1,6], [8,10], [15,18]]

(Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].)

Example 2:

Input: intervals = [[1,4], [4,5]]

Output: [[1,5]]
"""

def merge(intervals):
  merged = []
  intervals.sort() # N log n to make this problem easier

  for index, interval in enumerate(intervals):
    if not merged or merged[-1][1] < interval[0]
      merged.append(interval)
    else:
      merged[-1][1] = max(merged[-1][1],  interval[1])
  return merged
