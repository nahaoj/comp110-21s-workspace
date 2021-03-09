"""EX03 - prime functions."""

__author__: str = "930410205"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(int: int) -> bool:
    """Checks if a number is a prime number."""
    if int <= 1:
        return False
    for i in range(2, int):
        if int % i == 0:
            return False
    else:
        return True


def list_primes(int1: int, int2: int) -> list[int]:
    """Lists the prime numbers in between 2 integers."""
    prime_list: list[int] = [] 
    for number in range(int1, int2):
        if is_prime(number) == True:
            prime_list.append(number)
    else:
        return prime_list


if __name__ == "__main__":
    main()