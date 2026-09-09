import random


class RandomizedCollection:

    def __init__(self):
        # List containing all values, including duplicates
        self.nums = []

        # val -> set of indices where val occurs
        self.index_map = {}

    def insert(self, val: int) -> bool:

        # Was this value already present?
        is_new = val not in self.index_map

        # Add value to the list
        self.nums.append(val)

        # Create set if necessary
        if val not in self.index_map:
            self.index_map[val] = set()

        # Store index of this occurrence
        self.index_map[val].add(len(self.nums) - 1)

        return is_new

    def remove(self, val: int) -> bool:

        # Value doesn't exist
        if val not in self.index_map or not self.index_map[val]:
            return False

        # Get any index where val occurs
        remove_index = self.index_map[val].pop()

        # Last element in the list
        last_index = len(self.nums) - 1
        last_val = self.nums[last_index]

        # If we're NOT removing the last element,
        # move last_val into remove_index
        if remove_index != last_index:

            self.nums[remove_index] = last_val

            # Update last_val's index set
            self.index_map[last_val].remove(last_index)
            self.index_map[last_val].add(remove_index)

        # Remove last element
        self.nums.pop()

        # Remove empty set from dictionary
        if not self.index_map[val]:
            del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
