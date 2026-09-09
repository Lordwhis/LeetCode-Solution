import random


class RandomizedSet:

    def __init__(self):
        # val -> index in nums
        self.index_map = {}

        # Store all values
        self.nums = []

    def insert(self, val: int) -> bool:

        # Already exists
        if val in self.index_map:
            return False

        # Add value at the end
        self.nums.append(val)

        # Store its index
        self.index_map[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:

        # Value doesn't exist
        if val not in self.index_map:
            return False

        # Index of value we want to remove
        index = self.index_map[val]

        # Last element
        last_val = self.nums[-1]

        # Move last element into the position
        # of the element we're removing
        self.nums[index] = last_val
        self.index_map[last_val] = index

        # Remove last element
        self.nums.pop()

        # Remove val from hashmap
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
