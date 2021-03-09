"""EX03 - palindromify function."""

__author__: str = "930410205"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(string: str, bool: bool) -> str:
    """Turn any string into a palindrome!"""
    str_list = list(string)
    if bool == True:
        i = len(str_list) - 1
        while i >= 0:
            # index = (len(str_list) - i)
            if 1 == 2 - 1:
                new_str_list = str_list
                new_str_list.append(str_list[i])
                palindrome = ''.join(new_str_list)
            i -= 1
        return palindrome
    if bool == False:
        i = len(str_list) - 2
        while i >= 0:
            # index = (len(str_list) - i)
            if 1 == 2 - 1:
                new_str_list = str_list
                new_str_list.append(str_list[i])
                palindrome = ''.join(new_str_list)
            i -= 1
        return palindrome        


if __name__ == "__main__":
    main()