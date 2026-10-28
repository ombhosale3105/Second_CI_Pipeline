def rotate_string(text: str, k: int) -> str:
    """Rotate text right by k positions; negative k rotates left."""
    if not text:
        return text
    k %= len(text)
    return text[-k:] + text[:-k] if k else text


if __name__ == "__main__":
    sample = input("Enter a string: ")
    positions = int(input("Rotate right by how many positions? "))
    print(rotate_string(sample, positions))
