from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime, inverse, GCD

# Use small safe values for simplicity
p = 23  # prime
g = 5   # generator

# Alice
a = 6  # private
A = pow(g, a, p)  # public

# Bob
b = 15
B = pow(g, b, p)

# Shared secret
alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)

print("Alice public:", A)
print("Bob public:", B)
print("Shared secret (Alice):", alice_secret)
print("Shared secret (Bob):", bob_secret)
