import random


def get_random_range(start: int, stop: int) -> int:
    """
    returns a number between start (included) and stop (not included)
    :param start: int: number included
    :param stop: int: number not included
    :return: int: number between start and stop
    """
    number = random.randrange(start, stop)
    return number


def get_randint(start: int, stop: int) -> int:
    """
    returns a number between start (included) and stop (included)
    :param start: int: number included
    :param stop: int: number included
    :return: number between start and stop
    """
    number = random.randint(start, stop)
    return number


def get_shuffle(my_list: list) -> list:
    """
    The elements of my_list are mixed in a random order.
    :param my_list: list:
    :return: list:
    """
    random.shuffle(my_list)
    return my_list


if __name__ == "__main__":
    num = get_random_range(1, 9)
    num2 = get_randint(1, 9)
    print(num, num2)
    liste = get_shuffle([1, 2, 3, 4])
    print(liste)
