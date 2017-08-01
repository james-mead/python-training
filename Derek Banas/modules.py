# You can import by listing the file name minus the py
import sum
 
# Get access to functions by proceeding with the file
# name and then the function you want
print("Sum :", sum.getSum(1,2,3,4,5))
 
# ---------- FROM ----------
 
# You can use from to copy specific functions from a module
# You can use from sum import * to import all functions
# You can import multiple functions by listing them after
# import separated by commas
from sum import getSum
 
# You don't have to reference the module name now
print("Sum :", getSum(1,2,3,4,5))