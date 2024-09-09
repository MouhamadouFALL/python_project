
""" Simple testing example """

import random


def add_three(x: int) -> int:
    return x + 3

def remove_tree(x: int) -> int:
    return x - 3

def multiply_by_two(x: int) -> int:
    return x * 2

def main():
    # testing the function add_three

    assert add_three(1) == 4
    assert add_three(2) == 5
    assert add_three(3) == 6
    assert multiply_by_two(2) == 4
    assert multiply_by_two(3) == 6
    for _ in range(100):
        x = random.randint(-1000, 1000)
        assert add_three(remove_tree(x)) == x
    print("All tests pass!")


if __name__ == "__main__":
    main()
