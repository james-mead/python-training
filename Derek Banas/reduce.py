# ---------- REDUCE ----------
# Reduce receives a list and returns a single result
 
# You must import reduce
from functools import reduce
 
# Add up the values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))