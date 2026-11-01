def is_pangram(sentence: str) -> bool:
    """Return True when sentence contains every English letter at least once."""
    letters = {char.lower() for char in sentence if char.isalpha() and char.isascii()}
    return set("abcdefghijklmnopqrstuvwxyz").issubset(letters)


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Pangram" if is_pangram(text) else "Not a pangram")
