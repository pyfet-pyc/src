from algorithms.maths.polynomial import (
	Polynomial as  po,
)
from algorithms.maths.polynomial import (
	Monomial as mo,
)
from fractions import Fraction
import math


import unittest

class TestSuite(unittest.TestCase):

	def setUp(self):
		self.p0 = Polynomial([
			Monomial({})
		])
