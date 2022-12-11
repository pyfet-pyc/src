def __repr__(self):
    suites = '♠♥♣♦'
    faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return f'{suites[self.suite.value]}{faces[self.face]}'
