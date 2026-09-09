from typing import List
from bisect import bisect_left


class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:

        # Find where value would be inserted
        i = bisect_left(self.intervals, [value, value])

        # Check the interval on the LEFT
        if i > 0:
            left = self.intervals[i - 1]

            # value is already inside left interval
            if left[0] <= value <= left[1]:
                return

        # Check the interval on the RIGHT
        if i < len(self.intervals):
            right = self.intervals[i]

            # value is already inside right interval
            if right[0] <= value <= right[1]:
                return

        # Can connect to left interval?
        left_merge = (
            i > 0 and
            self.intervals[i - 1][1] + 1 == value
        )

        # Can connect to right interval?
        right_merge = (
            i < len(self.intervals) and
            self.intervals[i][0] - 1 == value
        )

        if left_merge and right_merge:
            # Merge:
            # [left_start, value] + [value, right_end]
            self.intervals[i - 1][1] = self.intervals[i][1]
            self.intervals.pop(i)

        elif left_merge:
            # Extend left
            self.intervals[i - 1][1] = value

        elif right_merge:
            # Extend right
            self.intervals[i][0] = value

        else:
            # Create new interval
            self.intervals.insert(i, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
