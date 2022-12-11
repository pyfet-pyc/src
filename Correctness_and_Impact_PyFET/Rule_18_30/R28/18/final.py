# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:17:05
# Size of source mod 2**32: 1343 bytes
"""Email address parsing code.

Lifted directly from rfc822.py.  This should eventually be rewritten.
"""
__all__ = [
 'mktime_tz',
 'parsedate',
 'parsedate_tz',
 'quote']
import time, calendar
SPACE = ' '
EMPTYSTRING = ''
COMMASPACE = ', '
_monthnames = [
 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul',
 'aug', 'sep', 'oct', 'nov', 'dec',
 'january', 'february', 'march', 'april', 'may', 'june', 'july',
 'august', 'september', 'october', 'november', 'december']
_daynames = [
 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
_timezones = {'UT':0, 
 'UTC':0,  'GMT':0,  'Z':0,  'AST':-400, 
 'ADT':-300,  'EST':-500, 
 'EDT':-400,  'CST':-600, 
 'CDT':-500,  'MST':-700, 
 'MDT':-600,  'PST':-800, 
 'PDT':-700}
# okay decompiling testbed_py/test.py
