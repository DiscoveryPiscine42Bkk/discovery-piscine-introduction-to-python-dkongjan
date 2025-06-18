import sys

if len(sys.argv) < 3:
    print("three two one")
else:
    for pram in reversed (sys.argv[1:]):
        print(pram)