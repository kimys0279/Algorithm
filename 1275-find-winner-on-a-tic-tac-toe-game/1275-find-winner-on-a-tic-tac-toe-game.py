class Solution(object):
    def tictactoe(self, moves):
        rows, cols = [0] * 3, [0] * 3
        d1, d2 = 0, 0
        player = 1
        
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c:
                d1 += player
            if r + c == 2:
                d2 += player
           
            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(d1) == 3 or abs(d2) == 3:
                if player == 1:
                    return 'A'
                else:
                    return 'B'
            player *= -1
            
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'
        
        
        # row [0]
        # one row or one col or any diag
        # player A : 1 / player B : -1