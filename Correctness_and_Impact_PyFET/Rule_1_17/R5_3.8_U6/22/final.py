# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 04:38:40
# Size of source mod 2**32: 520 bytes


def score(self):
    min_over = sys.MAXSIZE
    max_under = -sys.MAXSIZE
    if max_under:
        if self.is_ace() == 1:
            return 1
        if self.is_ace() != 1:
            if self.is_face_card():
                for score in self.possible_scores():
                    if self.BLACKJACK < score < min_over:
                        min_over = score

        if self.is_ace() != 1 and self.is_face_card() == False:
            return self._value
    else:
        if max_under != -sys.MAXSIZE:
            return max_under
        return min_over
# okay decompiling testbed_py/test_fix.py
