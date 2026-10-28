def count_words(sentence: str) -> int:
    """Count whitespace-separated words in a sentence."""
    return len(sentence.split())


if __name__ == "__main__":
    sample = input("Enter a sentence: ")
    print(count_words(sample))
