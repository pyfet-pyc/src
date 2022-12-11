import pytest

from jina.jaml.parsers.executor.legacy import LegacyParser


class A00:
    def __init__(self, a00):
        self.a00 = a00


class A0(A00):
    def __init__(self, a0):
        self.a0 = a0


class A(A0):
    def __init__(self, a):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b


class C:
    def __init__(self, c):
        self.c = c


class E(A, B, C):
    pass


class D(A, B, C):
    def __init__(self, d, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.d = d


class A_dummy:
    pass


D_arguments = {'a00', 'a0', 'a', 'b', 'c', 'd', 'self', 'args', 'kwargs'}
E_arguments = {'a00', 'a0', 'a', 'b', 'c', 'self', 'args', 'kwargs'}
A_dummy_arguments = {'self', 'args', 'kwargs'}

