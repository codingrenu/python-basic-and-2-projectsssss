import os

if os.path.exists("myyfile.txt"):
    os.remove("myyfile.txt")
    print("file deleted successfully ")
else:
    print("file doesn't exist")
