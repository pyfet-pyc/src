# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:49:19


def dumps(params, methodname=None, methodresponse=None, encoding=None, allow_none=False):
    """data [,options] -> marshalled data

    Convert an argument tuple or a Fault instance to an XML-RPC
    request (or response, if the methodresponse option is used).

    In addition to the data object, the following options can be given
    as keyword arguments:

        methodname: the method name for a methodCall packet

        methodresponse: true to create a methodResponse packet.
        If this option is used with a tuple, the tuple must be
        a singleton (i.e. it can contain only one element).

        encoding: the packet encoding (default is UTF-8)

    All byte strings in the data structure are assumed to use the
    packet encoding.  Unicode strings are automatically converted,
    where necessary.
    """
    assert isinstance(params, (tuple, Fault)), 'argument must be tuple or Fault instance'
    if FastMarshaller:
        m = FastMarshaller(encoding)
    else:
        m = Marshaller(encoding, allow_none)
    data = m.dumps(params)
    if encoding != 'utf-8':
        xmlheader = "<?xml version='1.0' encoding='%s'?>\n" % str(encoding)
    else:
        xmlheader = "<?xml version='1.0'?>\n"
    if methodname:
        data = (
         xmlheader,
         '<methodCall>\n<methodName>',
         methodname, '</methodName>\n',
         data,
         '</methodCall>\n')
    elif methodresponse:
        data = (
         xmlheader,
         '<methodResponse>\n',
         data,
         '</methodResponse>\n')
    else:
        return data
    return ('').join(data)
# okay decompiling testbed_py/test.py
