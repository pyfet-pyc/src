def _traverse_l(self, start, stop, step, color, l, skip=[]):
    moves = {}
    last = []

    current = self.board[r][l]
    if current == 0:
        if skip and not last:
            for r in range(start, stop, step):
                if l < 0:
                    break           
        tmp = skip and last and skip is None
        if tmp:
            return
    else:
        moves[(r, l)] = last

    if last:
        if step == -1:
            row = max(r - 3, 0)
        else:
            row = min(r + 3, rows)
        moves.update(
            self._traverse_l(r + step, row, step, color, l - 1, skip=last)
        )
        moves.update(
            self._traverse_r(r + step, row, step, color, l + 1, skip=last)
        )

        last = [current]
    l -= 1
    return moves