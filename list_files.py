import os

print("THe files and folders in {} are:".format(os.getcwd()))
items = os.listdir(".")
for item in items:
    print(item)