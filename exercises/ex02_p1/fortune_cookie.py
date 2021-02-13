"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "930410205"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())

    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:

    message: int = randint(1, 4)

    if int(message) == 1:  
        return "good things come to those who wait."
    else:
        if int(message) == 2:
            return "the higher the climb, the harder the fall."
        else:
            if int(message) == 3:
                return "give a man a fish, feed him for a day. teach a man to fish, feed him for a lifetime."
            else:
                return "with great power comes great responsibility."

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
