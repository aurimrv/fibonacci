# Fibonacci TDD Example

This is a simple example, adapted from [Kent Beck, 2003](https://www.amazon.com.br/Test-Driven-Development-Kent-Beck/dp/0321146530), to illustrate the TDD cycle.

The files are numbered according to the steps we followed. To run each test, just type the command below:

```
python -m testsXX.py
```
Where XX is the number of the test set to be executed. For instance, by running:

```
python -m tests01.py
```
is expected to get the following output:

```
$ python -m unittest tests01.py 
F
======================================================================
FAIL: test_fib01 (tests01.FibonacciTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/auri/insync/tdd/fibonacci/tests01.py", line 7, in test_fib01
    self.assertEqual(MathSamples.fibonacci(0), 0)
AssertionError: None != 0

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```
