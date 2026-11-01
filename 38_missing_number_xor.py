def missing_number_xor(numbers: list[int]) -> int:
    """Find the missing number from the range 0..n, with exactly one missing."""
    n = len(numbers)
    result = n
    for index, number in enumerate(numbers):
        result ^= index
        result ^= number
    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers from 0 to n with one missing: ").split()))
    print("Missing number:", missing_number_xor(numbers))
