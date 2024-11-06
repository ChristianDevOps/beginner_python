def add(a: int, b: int) -> int:
    """
    Adds the sum of two numbers.

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The sum of `a` and `b`
    """
    return a + b


if __name__ == '__main__':
    a: int = 4
    b: int = 8

    result: int = add(a, b)
    print(result)
