from typing import Sequence


def is_sorted(values: Sequence) -> bool:
    """Return True if values are in non-decreasing (ascending) order."""
    return all(values[index] <= values[index + 1] for index in range(len(values) - 1))


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("List is sorted" if is_sorted(numbers) else "List is not sorted")
