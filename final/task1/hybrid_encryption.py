# hybrid_encryption.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import os

# Step 1: Generate RSA key pair for User A
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("userA_private.pem", "wb") as f:
    f.write(private_key)
with open("userA_public.pem", "wb") as f:
    f.write(public_key)

# Step 2: User B encrypts message
message = b"This is a top secret message."
with open("message.txt", "wb") as f:
    f.write(message)

# Generate AES key
aes_key = get_random_bytes(32)  # AES-256
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

# Encrypt AES key with RSA
recipient_key = RSA.import_key(open("userA_public.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_aes_key = cipher_rsa.encrypt(aes_key)

# Write files
with open("encrypted_message.bin", "wb") as f:
    f.write(cipher_aes.nonce + tag + ciphertext)

with open("aes_key_encrypted.bin", "wb") as f:
    f.write(enc_aes_key)

# Step 3: User A decrypts
private_key = RSA.import_key(open("userA_private.pem").read())
cipher_rsa = PKCS1_OAEP.new(private_key)

dec_aes_key = cipher_rsa.decrypt(enc_aes_key)

with open("encrypted_message.bin", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher_aes = AES.new(dec_aes_key, AES.MODE_EAX, nonce=nonce)
decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag)

with open("decrypted_message.txt", "wb") as f:
    f.write(decrypted_message)
