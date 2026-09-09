class LFUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.freq = 1
            self.prev = None
            self.next = None

    class DoublyLinkedList:
        def __init__(self):
            self.head = LFUCache.Node(0, 0)
            self.tail = LFUCache.Node(0, 0)

            self.head.next = self.tail
            self.tail.prev = self.head

            self.size = 0

        def add_first(self, node):
            node.next = self.head.next
            node.prev = self.head

            self.head.next.prev = node
            self.head.next = node

            self.size += 1

        def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

            self.size -= 1

        def remove_last(self):
            if self.size == 0:
                return None

            node = self.tail.prev
            self.remove(node)

            return node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # key -> Node
        self.key_to_node = {}

        # frequency -> DoublyLinkedList
        self.freq_to_list = {}

        # Smallest frequency currently in cache
        self.min_freq = 0

    def _increase_frequency(self, node):
        old_freq = node.freq

        # Remove node from old frequency list
        old_list = self.freq_to_list[old_freq]
        old_list.remove(node)

        # If this was the last node with min_freq,
        # min_freq increases
        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        # Increase frequency
        node.freq += 1
        new_freq = node.freq

        # Create list for new frequency if necessary
        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = self.DoublyLinkedList()

        # Add as most recently used in new frequency
        self.freq_to_list[new_freq].add_first(node)

    def get(self, key: int) -> int:

        # Key doesn't exist
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        # Access increases frequency
        self._increase_frequency(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Edge case: capacity is 0
        if self.capacity == 0:
            return

        # Key already exists
        if key in self.key_to_node:
            node = self.key_to_node[key]

            # Update value
            node.value = value

            # put() also increases frequency
            self._increase_frequency(node)

            return

        # Cache is full -> evict LFU
        if self.size == self.capacity:

            # Get list containing minimum frequency
            min_list = self.freq_to_list[self.min_freq]

            # Within same frequency, remove LRU
            lru_node = min_list.remove_last()

            # Remove from key dictionary
            del self.key_to_node[lru_node.key]

            self.size -= 1

        # Create new node
        node = self.Node(key, value)

        # New keys always start with frequency 1
        self.key_to_node[key] = node

        # Add frequency-1 list if necessary
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = self.DoublyLinkedList()

        # New node is most recently used
        self.freq_to_list[1].add_first(node)

        # New minimum frequency is 1
        self.min_freq = 1

        self.size += 1
