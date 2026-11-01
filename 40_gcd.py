def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor using Euclid's algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    first = int(input("Enter first integer: "))
    second = int(input("Enter second integer: "))
    print("GCD:", gcd(first, second))
