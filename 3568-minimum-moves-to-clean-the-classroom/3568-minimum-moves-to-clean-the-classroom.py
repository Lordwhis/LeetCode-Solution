from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = len(litter_id)

        k = len(litter_id)

        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        max_energy = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        sr, sc = start
        max_energy[sr][sc][0] = energy

        q = deque([(sr, sc, energy, 0)])

        moves = 0

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            for _ in range(len(q)):
                r, c, curr_energy, mask = q.popleft()

                if mask == full_mask:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    if curr_energy == 0:
                        continue

                    new_energy = curr_energy - 1
                    new_mask = mask

                    if (nr, nc) in litter_id:
                        new_mask |= 1 << litter_id[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    if max_energy[nr][nc][new_mask] >= new_energy:
                        continue

                    max_energy[nr][nc][new_mask] = new_energy
                    q.append((nr, nc, new_energy, new_mask))

            moves += 1

        return -1
