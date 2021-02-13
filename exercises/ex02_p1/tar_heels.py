"""Tar Heels exercise redux as a structured program."""

__author__ = "930410205"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(num: int) -> int:
    two = int(num) % 2
    seven = int(num) % 7 
    if seven == 0 and two == 0:
        return "TAR HEELS"
    else:
        if seven == 0:
            return "HEELS"
        else:
            if two == 0:
                return "TAR"
            else:
                return "CAROLINA"


if __name__ == "__main__":
    main()
