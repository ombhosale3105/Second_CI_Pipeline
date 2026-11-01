from typing import List


def move_zeros(values: list) -> list:
    """Return a new list with all zero values moved to the end, preserving order."""
    non_zeros = [value for value in values if value != 0]
    zeros = [value for value in values if value == 0]
    return non_zeros + zeros


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("After moving zeros:", move_zeros(numbers))
