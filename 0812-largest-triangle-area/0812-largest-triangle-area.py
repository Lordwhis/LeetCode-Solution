from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        points = sorted(points)
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        hull = lower[:-1] + upper[:-1]


        def area(p1, p2, p3):
            return abs(0.5 * (p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])))

        n = len(hull)
        max_area = 0
        for i in range(n):
            k = i + 2
            for j in range(i + 1, n):
                while k < n and area(hull[i], hull[j], hull[k]) < area(hull[i], hull[j], hull[(k + 1) % n]):
                    k += 1
                max_area = max(max_area, area(hull[i], hull[j], hull[k % n]))

        return max_area