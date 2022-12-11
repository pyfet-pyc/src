# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-13 19:03:42
# Size of source mod 2**32: 962 bytes


def get_detail_sentence(self, CP):
    if not CP.notCar:
        sentence_builder = 'openpilot upgrades your <strong>{car_model}</strong> with automated lane centering{alc} and adaptive cruise control{acc}.'
        acc = ''
        if self.min_enable_speed > 0:
            acc = f" <strong>while driving above {self.min_enable_speed * CV.MS_TO_MPH:.0f} mph</strong>"
            for col in StarColumns:
                self.row[col] = Star.FULL

        else:
            if CP.carName not in ('nissan', 'subaru', 'toyota') or CP.carName == 'toyota' and CP.openpilotLongitudinalControl:
                acc = ' <strong>that automatically resumes from a stop</strong>'
    tmp2 = CP.notCar
    if tmp2:
        if CP.carFingerprint == 'COMMA BODY':
            return "The body is a robotics dev kit that can run openpilot. <a href='https://www.commabody.com'>Learn more.</a>"
        return 'This notCar does not have a detail sentence'
# okay decompiling testbed_py/test.pyc
