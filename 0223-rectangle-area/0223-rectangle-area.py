class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) -> int:
        
        int_area = (max((min(ay2, by2)-max(ay1, by1)),0)*               
                    max((min(ax2, bx2)-max(ax1, bx1)),0))               
                       
        return ((ax2-ax1)*(ay2-ay1) +                                  
                (bx2-bx1)*(by2-by1) -                                   
                int_area              )                                