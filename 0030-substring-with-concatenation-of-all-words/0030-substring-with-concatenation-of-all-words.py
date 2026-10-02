from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        total = k * len(words)
        target = Counter(words)
        words_counter = [target.copy() for _ in range(k)]
        res = []

        def helper(counter, word, count):
            counter[word] = counter.get(word, 0) + count

            if counter[word] == 0:
                del counter[word]

        # preload words
        for off in range(k):
            for j in range(off, off + total - k, k):
                word = s[j:j + k]
                helper(words_counter[off], word, -1)

        # rolling windows
        for i in range(len(s) - total + 1):
            off = i % k
            r = i + total - k
            word = s[r:r + k]
            helper(words_counter[off], word, -1)

            if not words_counter[off]:
                res.append(i)

            word = s[i:i + k]
            helper(words_counter[off], word, 1)

        return res