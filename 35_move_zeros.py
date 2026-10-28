def move_zeros(numbers: list) -> list:
    """Return a new list with all zeros moved to the end."""
    non_zeros = [number for number in numbers if number != 0]
    zeros = [number for number in numbers if number == 0]
    return non_zeros + zeros


if __name__ == "__main__":
    sample = input("Enter numbers separated by spaces: ")
    numbers = [int(value) for value in sample.split()]
    print(move_zeros(numbers))
