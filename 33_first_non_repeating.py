from collections import Counter
from typing import Optional


def first_non_repeating(text: str) -> Optional[str]:
    """Return the first character occurring once, or None if there is none."""
    counts = Counter(text)
    for char in text:
        if counts[char] == 1:
            return char
    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    result = first_non_repeating(text)
    print("First non-repeating character:", result if result is not None else "None")
