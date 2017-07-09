"""Hidden password example."""
import getpass

def requestPassword():
    """Request Password."""
    correctPassword = 'santa'
    # key = raw_input("Enter passsword: ")  # enter password in plain text
    key = getpass.getpass()

    if key == correctPassword:
        return True
    return False


if requestPassword():
    print("Welcome to the hidden code")
    x = 7
    print(x)
