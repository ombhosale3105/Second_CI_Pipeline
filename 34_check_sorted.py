def is_sorted(numbers: list) -> bool:
    """Return True if numbers are in non-decreasing order."""
    return all(numbers[index] <= numbers[index + 1] for index in range(len(numbers) - 1))


if __name__ == "__main__":
    sample = input("Enter numbers separated by spaces: ")
    numbers = [float(value) for value in sample.split()]
    print(is_sorted(numbers))
