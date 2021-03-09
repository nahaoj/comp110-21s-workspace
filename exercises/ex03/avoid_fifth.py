"""EX03 - avoid_fifth function."""

__author__: str = "930410205"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(string: str) -> str:
    """Removes the letter E/e from any string."""
    # string: str = str(input())
    string_list = list(string)
    i: int = 0
    while i < (len(string_list) - 1):
        letter = ord(string_list[i])
        e = ord('e')
        E = ord('E')
        if letter == e:
            string_list.pop(i)
            new_str = ''.join(string_list)
        elif letter == E:
            string_list.pop(i)
            new_str = ''.join(string_list)
        if ord(string_list[len(string_list) - 1]) == ord("e"):
            string_list.pop(len(string_list) - 1)
            new_str = ''.join(string_list)
        elif ord(string_list[len(string_list) - 1]) == ord("E"):
            string_list.pop(len(string_list) - 1)
            new_str = ''.join(string_list)
        i += 1
    return new_str

    
if __name__ == "__main__":
    main()