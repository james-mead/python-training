"""Example of keyboard input."""
import Tkinter
import tkSimpleDialog

def key_input(message):
    root = Tkinter.Tk()
    root.withdraw()
    value = tkSimpleDialog.askstring("window", message)
    return value


firstName = key_input("Enter firstname:\n")
lastName = key_input("Enter lastname:\n")  # with pyhton 3, just enter input()
age = key_input("Enter age:\n")

print(firstName, lastName, age)
