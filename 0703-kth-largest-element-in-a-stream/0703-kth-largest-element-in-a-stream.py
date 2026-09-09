import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k

        # Min-heap containing the k largest elements
        self.heap = nums

        heapq.heapify(self.heap)

        # Keep only k elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # Keep exactly k largest elements
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Root is the kth largest
        return self.heap[0]
