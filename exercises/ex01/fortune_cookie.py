"""Program that outputs one of at least four random, good fortunes."""

__author__ = "930410205"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("your fortune cookie says...")

message: int = randint(1,4)

if int(message) == 1:
     print("good things come to those who wait.")
else:
         if int(message) == 2:
             print("the higher the climb, the harder the fall.")
         else:
                 if int(message) == 3:
                    print("give a man a fish, feed him for a day. teach a man to fish, feed him for a lifetime.")
                 else:
                        print("with great power comes great responsibility.")

print("now, go spread positive vibes!")
    