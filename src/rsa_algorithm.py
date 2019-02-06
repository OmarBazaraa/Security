import math

from src.utils import *


class RSA:

    def __init__(self):
        """
        Initializes RSA algorithm
        """
        self.__n = 0
        self.__e = 0
        self.__d = 0

    def generate_key(self, length=1000):
        """
        Generates the public and private keys for RSA algorithm.
        The length of the modulus for the public key and the private keys 'n' will
        be generated to be of about the given length +/- 1.

        :param length: the length of the key (must be greater than one).
        :return: n, e, d
        """

        # Assert key length to be greater than 1
        assert (length > 1)

        #
        # 1. Choose two different large random prime numbers 'p' and 'q'
        #
        if length == 2:
            primes = [2, 3, 5, 7]

            p = random.choice(primes)
            q = random.choice(primes)

            # Assure that 'p' and 'q' are different primes
            while q == p or p * q < 10:
                p = random.choice(primes)
                q = random.choice(primes)
        else:
            l = random.randint(1, max(1, length - 1))
            p = generate_prime(length - l)
            q = generate_prime(l)

            # Assure that 'p' and 'q' are different primes
            while q == p:
                q = generate_prime(l)

        #
        # 2. Calculate 'n = p.q'
        #    'n' is the modulus for the public key and the private keys
        #
        n = p * q

        #
        # 3. Calculate the Euler totient function of 'n'
        #    phi(n) = (p-1)(q-1)
        #
        phi = (p - 1) * (q - 1)

        #
        # 4. Choose an integer 'e' such that 1 < 'e' < phi(n), and 'e' is co-prime to phi(n)
        #    (i.e.: gcd(e, phi(n)) = 1)
        #    'e' is released as the public key exponent
        #
        e = random.randint(2, phi - 1)
        while math.gcd(e, phi) > 1:
            e = random.randint(2, phi - 1)

        #
        # 5. Compute 'd' to satisfy the congruence relation (d.e = 1 (mod phi(n)))
        #    (i.e.: d.e = 1 + k.phi(n), for some integer 'k').
        #    'd' is kept as the private key exponent
        #
        s, t = extended_euclid(e, phi)
        d = ((s % phi) + phi) % phi

        # Assert that 'd' is the modular inverse of 'e' modulo 'phi(n)'
        assert ((d * e) % phi == 1)

        # Return the generated keys
        self.__n = n
        self.__e = e
        self.__d = d
        return n, e, d

    def encrypt(self, message):
        return pow(message, self.__e, self.__n)

    def decrypt(self, cipher):
        return pow(cipher, self.__d, self.__n)

    def get_public_key(self):
        return self.__e, self.__n
