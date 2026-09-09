class LRUCache:

    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = self.Node()  # Most recently used side
        self.tail = self.Node()  # Least recently used side

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add_to_front(self, node):
        """Add node right after head."""
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Recently accessed => move to front
        self.remove(node)
        self.add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]

            node.value = value

            # Updated key becomes most recently used
            self.remove(node)
            self.add_to_front(node)

            return

        # Create new node
        node = self.Node(key, value)

        self.cache[key] = node
        self.add_to_front(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:
            # Least recently used node is before tail
            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]
