import random


def check_prime(n):
    """
    Checks and returns whether the given number 'n' is prime or not.

    :param n: the number to check its primality
    :return: true if the given number is a prime, false otherwise.
    """
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def miller_rabin(n, t=20):
    """
    Checks and returns whether the given number 'n' is prime or not
    using a probabilistic method.

    The probability that the algorithm fails is less than (0.25^t).

    :param n: the number to check its primality
    :param t: the number of iterations
    :return: true if the given number is a probable prime, false otherwise.
    """
    # Number 2 is the only even prime number
    if n == 2:
        return True

    # Other even numbers are composite
    if n < 2 or (n & 1) == 0:
        return False

    # Probabilistic primality check
    # Returns false if the given number 'n' is composite number,
    # Returns true if the given number 'n' is a probable prime number.
    def check(a, k, q, n):
        x = pow(a, q, n)

        if x == 1:
            return True

        for i in range(k):
            if x == n - 1:
                return True

            x = (x * x) % n

        return False

    #
    # Compute coefficients k, q: "n - 1 = power(2, k) * q"
    #
    k = 0
    q = n - 1
    while (q & 1) == 0:
        q >>= 1
        k += 1

    #
    # Probabilistic primality check for t-time
    #
    for i in range(t):
        a = random.randint(2, n - 1)
        if not check(a, k, q, n):
            return False

    return True


def generate_prime(length):
    """
    Generates a prime number of the given length.

    :param length: the length of the prime number to generate.
    :return: the generated prime number of length close to the given length.
    """
    l = pow(10, max(0, length - 1))
    r = l * 10

    x = random.randint(l, r - 1)

    p = x
    while p < r:
        if miller_rabin(p):
            return p
        p += 1

    p = x - 1
    while p > l:
        if miller_rabin(p):
            return p
        p -= 1

    assert False


def extended_euclid(a, b):
    """
    Calculate the Bezout's coefficients ('s' and 't') of the given 'a' and 'b'.
    That is, the coefficients of the smallest positive linear combination of 'a' and 'b'.
    (i.e. gcd(a, b) = s.a + t.b)

    :param a:
    :param b:
    :return: the Bezout's coefficients ('s' and 't').
    """
    if b == 0:
        return 1, 0

    s, t = extended_euclid(b, a % b)
    return t, s - t * int(a // b)
