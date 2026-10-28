from collections import Counter


def first_non_repeating(text: str):
    """Return the first character that occurs once, or None if there isn't one."""
    counts = Counter(text)
    for char in text:
        if counts[char] == 1:
            return char
    return None


if __name__ == "__main__":
    sample = input("Enter a string: ")
    result = first_non_repeating(sample)
    print(result if result is not None else "No non-repeating character")
