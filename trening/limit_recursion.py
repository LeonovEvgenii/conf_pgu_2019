from pyDatalog import pyDatalog

pyDatalog.create_terms('factorial, N, X, Y, Z, M, fff')


fff(Z, M) <= (Z==M*2)
factorial(3, X) <= (X==3+Z) & fff(Z, 2)

print(factorial(3, X))





factorial(3, 4)
factorial(3, X) <= (X==3+3)

print(factorial(3, X))





#################
# factorial(N, Y, X) <= (X==Y*2) & (N>0)

# print(factorial(1, 10, X))





# + factorial(1, 1)
# factorial(N, X) <= (X==N+Z) & (factorial(N-1, Z)) & (N>1)

# print(factorial(3, X))