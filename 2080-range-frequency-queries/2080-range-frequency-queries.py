from collections import defaultdict
from bisect import bisect_left, bisect_right


class RangeFreqQuery:

    def __init__(self, arr):
        self.positions = defaultdict(list)

        for i, value in enumerate(arr):
            self.positions[value].append(i)

    def query(self, left, right, value):
        indices = self.positions[value]

        # First index >= left
        start = bisect_left(indices, left)

        # First index > right
        end = bisect_right(indices, right)

        return end - start
