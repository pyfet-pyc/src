def score(self):
    min_over = sys.MAXSIZE
    max_under = -sys.MAXSIZE
    if max_under:
        if self.is_ace() == 1:
            return 1
        elif self.is_face_card():
            for score in self.possible_scores():
                if self.BLACKJACK < score < min_over:
                    min_over = score
        else:
            return self._value
        
    else:
        return max_under if max_under != -sys.MAXSIZE else min_over
