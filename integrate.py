import numpy as np
from random import sample

base = 3
side = base * base

sq = side * side # = 81
em = sq * 3//4
print(em)

print(len(sample(range(sq),em))) # random samples from range of squares
print(base//side)
print(base%side)
print(len(str(side)))
print(*(f"{n or '':{1}}"for n in len(str(side))))