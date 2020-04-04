"""
Example 1-b. Methods of optimization

1-b__optimization.py
"""

#Base Python Code
loops = 25000000
from math import *
a = range(1, loops)
def f(x):
    return 3 * log(x) + cos(x) ** 2

%timeit r = [f(x) for x in a]
#23.1 ± 6.99 seconds per loop

#Using NumPy
import numpy as np
a = np.arange(1, loops)
%timeit r = 3 * np.log(a) + np.cos(a) ** 2
#1.23 s ± 79.7 ms per loop

#Using NumExpr
import numexpr as ne
ne.set_num_threads(1)
f = "3 * log(a) + cos(a) ** 2"
%timeit r = ne.evaluate(f)
#452 ms ± 13.2 ms per loop

#Using NumExpr, but use parallel processing
ne.set_num_threads(4)
%timeit r = ne.evaluate(f)
#239 ms ± 30.7 ms per loop