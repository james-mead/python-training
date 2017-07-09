"""Hidden password example."""
import Tkinter
import tkSimpleDialog

def requestPassword():
    """Request Password."""
    correctPassword = 'santa'

    root = Tkinter.Tk()
    root.withdraw()

    key = tkSimpleDialog.askstring("Password", "Enter password", show="*")

    if key == correctPassword:
        return True
    return False


if requestPassword():
    print("Welcome to the hidden code")
    x = 7
    print(x)
