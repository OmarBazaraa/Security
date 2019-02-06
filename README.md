# Security

Implementation of the RSA algorithm in Python.

RSA is an algorithm used by modern computers to encrypt and decrypt messages.  
It is an asymmetric cryptographic algorithm. Asymmetric means that there are two different keys.  
This is also called public key cryptography, because one of the keys can be given to anyone. The other key must be kept private.

## Algorithm steps
### 1. Keys generation
1. Choose two different large random prime numbers *__p__* and *__q__*.
2. Calculate *__n = p.q__*.  
   *__n__* is the modulus for the public key and the private keys.
3. Calculate the Euler totient of *__n__*: *__phi(n) = (p-1)(q-1)__*
4. Choose an integer *__e__* such that *__1 < e < phi(n)__*, and *__e__* is co-prime to *__phi(n)__*.  
   *__e__* is released as the public key exponent.
5. Compute *__d__* to satisfy the congruence relation (_**de** = 1 (**mod phi(n)**)_) (i.e.: *__d__* is the modular inverse of *__e__* modulo *__phi(n)__*).  
   *__d__* is kept as the private key exponent.

### 2. Encryption
To encrypt a message *__m__*:

*__c = pow(m, e) mod n__*

### 3. Decryption
To decrypt the ciphered message *__c__*:

*__m = pow(c, d) mod n__*

## How to use
1. Install Python 3 interpreter.
2. Clone this repository.
   ```Console
   git clone https://github.com/OmarBazaraa/Security.git
   ```
3. Install project dependencies.
   ```Console
   pip install -r requirements.txt
   ```
4. Run the project.
   ```Console
   python3 ./src/main.py
   ```
