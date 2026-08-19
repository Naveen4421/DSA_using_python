class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        rows = defaultdict(int)   
        
        
        for row, seat in reservedSeats:
            rows[row] |= 1 << (seat - 1)   
        
        
        LEFT  = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)   
        MID   = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6)   
        RIGHT = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8)   
        
        
        total = (n - len(rows)) * 2
        
        
        for mask in rows.values():
            can_left  = (mask & LEFT) == 0
            can_right = (mask & RIGHT) == 0
            can_mid   = (mask & MID) == 0
            
            if can_left and can_right:
                total += 2       
            elif can_left or can_mid or can_right:
                total += 1      
        
        return total
