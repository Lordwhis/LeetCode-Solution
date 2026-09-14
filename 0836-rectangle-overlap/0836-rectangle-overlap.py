class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        return min(x2, a2) > max(x1, a1) and \
               min(y2, b2) > max(y1, b1)