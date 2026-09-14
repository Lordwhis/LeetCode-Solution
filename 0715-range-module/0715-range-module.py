from bisect import bisect_left

class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        new_intervals = []
        i = 0
        n = len(self.intervals)

        # Add intervals completely before [left, right)
        while i < n and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1

        new_intervals.append([left, right])

        # Add remaining intervals
        new_intervals.extend(self.intervals[i:])

        self.intervals = new_intervals

    def queryRange(self, left, right):
        for start, end in self.intervals:
            if start > left:
                break

            if start <= left and right <= end:
                return True

        return False

    def removeRange(self, left, right):
        new_intervals = []

        for start, end in self.intervals:

            # Completely before [left, right)
            if end <= left:
                new_intervals.append([start, end])

            # Completely after [left, right)
            elif start >= right:
                new_intervals.append([start, end])

            else:
                # Keep the left part
                if start < left:
                    new_intervals.append([start, left])

                # Keep the right part
                if end > right:
                    new_intervals.append([right, end])

        self.intervals = new_intervals
