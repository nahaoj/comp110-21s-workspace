"""An exercise in remainders and boolean logic."""

__author__ = "930410205"


# Begin your solution here...
n: int = input()
print('Enter an integer: ' + n)
two = int(n) % 2
seven = int(n) % 7 
if seven == 0 and two == 0:
    print("TAR HEELS")
else:
    if seven == 0:
        print("HEELS")
    else:
        if two == 0:
            print("TAR")
        else:
            print("CAROLINA")
