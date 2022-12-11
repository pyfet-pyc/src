def remove(self, pieces):
    
    if piece != 0:
        if piece.color == black:
            self.black_l -= 1
            for piece in pieces:
                self.board[piece.row][piece.col] = 0
        tmp = piece.color != black and piece is None
        if tmp:
            return
    else:
        self.white_l -= 1