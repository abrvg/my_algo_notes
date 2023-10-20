"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.
"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
    
    # Traverse the list intervals
    n = len(intervals)

    results = []

    curr = 0
    prev = 0

    while curr < n :
        if intervals[curr][0] <= intervals[prev][1]:
            results.append([min(intervals[prev][0], intervals[curr][0]), max(intervals[prev][1], intervals[curr][1])])

        else:
            results.append(intervals[curr])

        prev = curr
        curr += 1

    return results

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[5,6]]))
    
