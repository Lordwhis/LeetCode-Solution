from typing import List


class StreamChecker:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self, words: List[str]):
        self.root = self.TrieNode()

        # Maximum word length
        self.max_len = 0

        # Store the stream
        self.stream = []

        # Build Trie using reversed words
        for word in words:
            self.max_len = max(self.max_len, len(word))

            node = self.root

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = self.TrieNode()

                node = node.children[ch]

            node.is_word = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        node = self.root

        # Start from the newest character
        # and move backwards through the stream
        for i in range(len(self.stream) - 1, max(-1, len(self.stream) - self.max_len - 1), -1):

            ch = self.stream[i]

            if ch not in node.children:
                return False

            node = node.children[ch]

            if node.is_word:
                return True

        return False
