class AllOne:

    class Bucket:
        def __init__(self, count=0):
            self.count = count
            self.keys = set()

            self.prev = None
            self.next = None

    def __init__(self):
        # key -> Bucket containing that key
        self.key_to_bucket = {}

        # Dummy head and tail
        self.head = self.Bucket()
        self.tail = self.Bucket()

        self.head.next = self.tail
        self.tail.prev = self.head

    # Insert bucket after prev_bucket
    def _insert_bucket(self, prev_bucket, count):
        bucket = self.Bucket(count)

        bucket.next = prev_bucket.next
        bucket.prev = prev_bucket

        prev_bucket.next.prev = bucket
        prev_bucket.next = bucket

        return bucket

    # Remove an empty bucket
    def _remove_bucket(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev

    def inc(self, key: str) -> None:

        # New key
        if key not in self.key_to_bucket:

            # Frequency starts at 1
            if self.head.next != self.tail and self.head.next.count == 1:
                bucket = self.head.next
            else:
                bucket = self._insert_bucket(self.head, 1)

            bucket.keys.add(key)
            self.key_to_bucket[key] = bucket

            return

        # Existing key
        current = self.key_to_bucket[key]
        next_count = current.count + 1

        # Find/create next frequency bucket
        if current.next != self.tail and current.next.count == next_count:
            next_bucket = current.next
        else:
            next_bucket = self._insert_bucket(current, next_count)

        # Move key
        current.keys.remove(key)
        next_bucket.keys.add(key)

        self.key_to_bucket[key] = next_bucket

        # Remove old bucket if empty
        if not current.keys:
            self._remove_bucket(current)

    def dec(self, key: str) -> None:

        current = self.key_to_bucket[key]

        # Frequency becomes 0 -> remove key
        if current.count == 1:
            current.keys.remove(key)
            del self.key_to_bucket[key]

            if not current.keys:
                self._remove_bucket(current)

            return

        prev_count = current.count - 1

        # Find/create previous frequency bucket
        if current.prev != self.head and current.prev.count == prev_count:
            prev_bucket = current.prev
        else:
            prev_bucket = self._insert_bucket(current.prev, prev_count)

        # Move key
        current.keys.remove(key)
        prev_bucket.keys.add(key)

        self.key_to_bucket[key] = prev_bucket

        # Remove old bucket if empty
        if not current.keys:
            self._remove_bucket(current)

    def getMaxKey(self) -> str:

        # Empty
        if self.tail.prev == self.head:
            return ""

        # Any key from highest-frequency bucket
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:

        # Empty
        if self.head.next == self.tail:
            return ""

        # Any key from lowest-frequency bucket
        return next(iter(self.head.next.keys))
