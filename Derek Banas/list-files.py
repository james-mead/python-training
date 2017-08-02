import os, glob

try:
    os.chdir("./")
    for file in glob.glob("*.py"):
        print(file)

except FileNotFoundError:
    print("File was not found")