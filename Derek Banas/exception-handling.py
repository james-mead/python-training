# ---------- EXCEPTION HANDLING ----------
# Exceptions are triggered either when an error occurs
# or when you want them to.
 
# We use exceptions are used to handle errors, execute
# specific code when code generates something out of
# the ordinary, to always execute code when something
# happens (close a file that was opened),
 
# When an error occurs you stop executing code and jump
# to execute other code that responds to that error
 
# Let's handle an IndexError exception that is
# triggered when you try to access an index in a list
# that doesn't exist
 
# Surround a potential exception with try
try:
    aList = [1,2,3]
 
    print(aList[3])
 
# Catch the exception with except followed by the
# exception you want to catch
 
# You can catch multiple exceptions by separating them
# with commas inside parentheses
# except (IndexError, NameError):
except IndexError:
    print("Sorry that index doesn't exist")
 
# If the exception wasn't caught above this will
# catch all others
except:
    print("An unknown error occurred")