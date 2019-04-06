from pyDatalog import pyDatalog
pyDatalog.create_terms('factorial, N, X, Y, increment')

import logging
from pyDatalog import pyEngine
pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

increment(X, Y) <= (Y==X+1)
factorial(X, Y) <= ((Y==1+N) & (increment(X, N)))

print(factorial(1, Y))

# factorial(X, Y) <= ((Y==X+N) & (factorial(X-1, N)))
# factorial(1, Y) <= (Y==1)

# print(factorial(3, Y))


#####################3

# factorial(N, X) <= (X+factorial(N-1, X-1))
# factorial(1, X) <= X

# print(factorial(3, 10))

# factorial[N, X] = X+factorial[N-1 ,X-1]
# factorial[1, X] = X

# print(factorial[3, 10]==X)

# factorial[N] = N*factorial[N-1]
# factorial[1] = 1

# print(factorial[3]==N)