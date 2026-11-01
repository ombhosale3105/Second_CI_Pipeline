from collections import Counter
from typing import Any, Optional


def most_frequent(values: list) -> Optional[Any]:
    """Return the most frequent item; ties are resolved by first appearance."""
    if not values:
        return None
    counts = Counter(values)
    highest_count = max(counts.values())
    return next(value for value in values if counts[value] == highest_count)


if __name__ == "__main__":
    values = input("Enter items separated by spaces: ").split()
    print("Most frequent element:", most_frequent(values))
