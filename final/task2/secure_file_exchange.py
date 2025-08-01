# secure_file_exchange.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from hashlib import sha256

# Bob generates RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

# Alice creates message
with open("alice_message.txt", "wb") as f:
    f.write(b"This is Alice's secret file.")

# AES encryption
aes_key = get_random_bytes(32)
iv = get_random_bytes(16)

cipher = AES.new(aes_key, AES.MODE_CFB, iv)
plaintext = open("alice_message.txt", "rb").read()
ciphertext = cipher.encrypt(plaintext)

with open("encrypted_file.bin", "wb") as f:
    f.write(iv + ciphertext)

# Encrypt AES key
recipient_key = RSA.import_key(open("public.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_key = cipher_rsa.encrypt(aes_key)

with open("aes_key_encrypted.bin", "wb") as f:
    f.write(enc_key)

# Bob decrypts
private_key = RSA.import_key(open("private.pem").read())
cipher_rsa = PKCS1_OAEP.new(private_key)
dec_key = cipher_rsa.decrypt(enc_key)

with open("encrypted_file.bin", "rb") as f:
    iv = f.read(16)
    ciphertext = f.read()

cipher = AES.new(dec_key, AES.MODE_CFB, iv)
decrypted = cipher.decrypt(ciphertext)

with open("decrypted_message.txt", "wb") as f:
    f.write(decrypted)

# Hash check
original_hash = sha256(open("alice_message.txt", "rb").read()).hexdigest()
decrypted_hash = sha256(open("decrypted_message.txt", "rb").read()).hexdigest()
assert original_hash == decrypted_hash
