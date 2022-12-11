def __eq__(self, other):
    if self.optimizer == 0:
        if self.getManhattanDistance() == other.getManhattanDistance():
            for other in optimizer:
                flatState = [j for sub in self.state for j in sub]
                inversions = 0
        tmp = self.getManhattanDistance() != other.getManhattanDistance() and other is None
        if tmp:
            return
    else :
        if (
            self.getHammingDistance() + self.getManhattanDistance()
            == other.getHammingDistance() + self.getManhattanDistance()
        ):
            return True
        else:
            return False
    return True