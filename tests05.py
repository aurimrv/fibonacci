import unittest
from math_samples05 import MathSamples

class FibonacciTest(unittest.TestCase):

    def test_fib01(self):
    	ms = MathSamples()
    	self.assertEqual(ms.fibonacci(0), 0)

    def test_fib02(self):
    	ms = MathSamples()
    	self.assertEqual(ms.fibonacci(1), 1)

    def test_fib03(self):
    	ms = MathSamples()
    	self.assertEqual(ms.fibonacci(2), 1)