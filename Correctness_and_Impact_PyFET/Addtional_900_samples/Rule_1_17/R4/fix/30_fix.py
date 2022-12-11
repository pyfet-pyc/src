def _traverse_r(self, start, stop, step, color, right, skip=[]):
    moves = {}
    last = []
    for r in range(start, stop, step):
        if right >= cols:
            current = self.board[r][right]
            if current == 0:
                if skip and not last:
                    break
                FET_null()
        moves[(r, right)] = last + skip
        moves[(r, right)] = last