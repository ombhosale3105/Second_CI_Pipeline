def rotate_string(text: str, k: int) -> str:
    """Rotate text left by k positions. Negative k rotates right."""
    if not text:
        return text
    k %= len(text)
    return text[k:] + text[:k]


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter rotation positions: "))
    print("Rotated string:", rotate_string(text, k))
