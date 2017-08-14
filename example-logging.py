"""Example of using logging."""
import logging

def addition(a, b):
    if a < 5:
        logging.warning("Less than 5")
    else:
        return ("OK")


addition(4, 3)
