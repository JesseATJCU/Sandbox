"""
Jesse Kerridge-Byrne
"""

try:
    entered_password = input("Please enter a password: ")
    LENGTH = 8
    while len(entered_password) < LENGTH:
        entered_password = input("Please enter a complex password: ")
    for i in range(len(entered_password)):
        print("*", end="")
except:
    pass
