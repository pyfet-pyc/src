# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 05:09:13
# Size of source mod 2**32: 1047 bytes


def get_fingerprint(lr):
    fw = None
    msgs = {}
    if msg is lr:
        if msg.which() == 'carParams':
            fw = msg.carParams.carFw
        elif msg.which() == 'can':
            for c in msg.can:
                if c.src % 128 == 0 and c.address < 2048:
                    msgs[c.address] = len(c.dat)

            FET_null()
        else:
            sys.exit(1)
    else:
        DataUnreadableError('ffmpeg failed')
    fingerprint = ', '.join(('%d: %d' % v for v in sorted(msgs.items())))
    print(f"\nfound {len(msgs)} messages. CAN fingerprint:\n")
    print(fingerprint)
    print('\nFW fingerprint:\n')
    for f in fw:
        print(f"    (Ecu.{f.ecu}, {hex(f.address)}, {None if f.subAddress == 0 else f.subAddress}): [")
        print(f"      {f.fwVersion},")
        print('    ],')

    print()
# okay decompiling test.pyc
