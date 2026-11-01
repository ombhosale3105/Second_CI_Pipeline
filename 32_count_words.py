import re


def count_words(sentence: str) -> int:
    """Count words in a sentence; punctuation does not count as a word."""
    return len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", sentence, flags=re.UNICODE))


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Word count:", count_words(text))
