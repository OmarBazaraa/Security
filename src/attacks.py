from src.utils import *


def brute_force(ciphered_message, rsa):
    # Get the public key
    e, n = rsa.get_public_key()

    # Factorize 'n' into its two prime factors: 'p' and 'q'
    p, q = 2, 3
    while p * p < n:
        if n % p == 0:
            q = int(n // p)
            break
        p += 1

    # Calculate phi(n)
    phi = (p - 1) * (q - 1)

    # Calculate the private key 'd'
    s, t = extended_euclid(e, phi)
    d = ((s % phi) + phi) % phi

    # Return the private key 'd'
    return pow(ciphered_message, d, n)


def chosen_cipher_text(ciphered_message, rsa):
    # Get the public key
    e, n = rsa.get_public_key()

    # Alter the ciphered message and ask for decryption
    c = (ciphered_message * rsa.encrypt(2)) % n
    m = rsa.decrypt(c)

    # Compute the only two possibilities of the original message
    mes1, mes2 = -1, -1
    if m % 2 == 0:
        mes1 = int(m // 2)
    if (n + m) % 2 == 0:
        mes2 = int((n + m) // 2)

    # Returns the two possibilities of the original message
    return mes1, mes2
