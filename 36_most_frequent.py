from collections import Counter


def most_frequent(numbers: list):
    """Return the most frequent element, or None for an empty list."""
    if not numbers:
        return None
    counts = Counter(numbers)
    highest_count = max(counts.values())
    return next(number for number in numbers if counts[number] == highest_count)


if __name__ == "__main__":
    sample = input("Enter values separated by spaces: ")
    values = sample.split()
    print(most_frequent(values))
