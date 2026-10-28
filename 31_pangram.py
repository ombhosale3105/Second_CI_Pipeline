def is_pangram(text: str) -> bool:
    """Return True when text contains every English letter at least once."""
    letters = {char.lower() for char in text if char.isalpha() and char.isascii()}
    return set("abcdefghijklmnopqrstuvwxyz").issubset(letters)


if __name__ == "__main__":
    sample = input("Enter a sentence: ")
    print(is_pangram(sample))
