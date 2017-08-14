
import Tkinter
import tkMessageBox

root = Tkinter.Tk()
root.withdraw()

# tkMessageBox.showinfo("Hello", "Hello World")  # simple window
age = tkMessageBox.askyesno("Prompt", "Are you 18 or above?")  # vote window

print(age)
