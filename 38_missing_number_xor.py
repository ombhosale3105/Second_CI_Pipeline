def missing_number(numbers: list[int]) -> int:
    """Return the missing value from 0..n, assuming one value is absent."""
    missing = len(numbers)
    for index, number in enumerate(numbers):
        missing ^= index ^ number
    return missing


if __name__ == "__main__":
    sample = input("Enter numbers from a range with one missing: ")
    numbers = [int(value) for value in sample.split()]
    print(missing_number(numbers))
