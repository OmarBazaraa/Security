import time
import random
import matplotlib.pyplot as plt
from src import attacks

from src.rsa_algorithm import RSA


REPLICAS = 50

key_len = []
encryption_time = []
brute_force_attack_time = []

#
# Compute encryption time for different key lengths
#
for l in range(2, 100):
    # Log
    print('Encryption > Running at length:', l)

    # Initialize values
    enc_time = 0

    # Run the algorithm for 'replicas'-times and average the results
    for i in range(REPLICAS):
        # Generate random RSA keys
        rsa = RSA()
        n, e, d = rsa.generate_key(l)

        # Generate random message
        mes = random.randint(1, n - 1)

        # Encrypt
        tic = time.clock()
        enc = rsa.encrypt(mes)
        toc = time.clock()
        enc_time += (toc - tic) * 1000

        # Decrypt
        dec = rsa.decrypt(enc)

        # Assert correct decryption
        if mes != dec:
            print()
            print('-------------------')
            print('Decryption Failed!!')
            print('-------------------')
            print()
            print('n =', n)
            print('e =', e)
            print('d =', d)
            print('mess =', mes)
            print('E[m] =', enc)
            print('D[c] =', dec)
            exit(0)

        # Chosen cipher text attack
        mes_1, mes_2 = attacks.chosen_cipher_text(enc, rsa)
        assert (mes == mes_1 or mes == mes_2)

    # Append values
    key_len.append(l)
    encryption_time.append(enc_time / REPLICAS)


#
# Compute brute force attack time for different key lengths
#
for l in range(2, 20):
    # Log
    print('BruteForce > Running at length:', l)

    # Initialize values
    bf_time = 0

    # Run the algorithm for 'replicas'-times and average the results
    for i in range(REPLICAS):
        # Generate random RSA keys
        rsa = RSA()
        n, e, d = rsa.generate_key(l)

        # Brute force attack
        tic = time.time()
        d_ = attacks.brute_force(rsa)
        toc = time.time()
        bf_time += (toc - tic) * 1000 * 1000
        assert (d == d_)

    # Append values
    brute_force_attack_time.append(bf_time / REPLICAS)


#
# Plot results
#

f1 = plt.figure()
plt.title('Key Length vs Encryption Time')
plt.xlabel('Key Length (log10(n))')
plt.ylabel('Time (milliseconds)')
plt.plot(key_len, encryption_time)

f2 = plt.figure()
plt.title('Key Length vs Brute Force Attack Time')
plt.xlabel('Key Length (log10(n))')
plt.ylabel('Time (seconds)')
plt.plot(key_len[:len(brute_force_attack_time)], brute_force_attack_time)

plt.show()
