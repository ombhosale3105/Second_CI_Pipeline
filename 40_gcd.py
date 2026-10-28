def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor of a and b."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))
    print(gcd(first, second))
