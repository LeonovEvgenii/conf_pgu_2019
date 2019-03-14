from pyDatalog import pyDatalog
pyDatalog.create_terms('factorial, N, X')

import logging
from pyDatalog import pyEngine
pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

factorial[N, X] = X+factorial[N-1 ,X-1]
factorial[1, X] = X

print(factorial[3, 10]==X)

# factorial[N] = N*factorial[N-1]
# factorial[1] = 1

# print(factorial[3]==N)