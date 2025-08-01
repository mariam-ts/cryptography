Encryption Flow:
1. User A creates RSA key pair and shares public key.
2. User B generates AES-256 key, encrypts message.
3. AES key is encrypted with RSA public key.
4. User A decrypts AES key with private RSA key.
5. AES key is used to decrypt the original message.

This demonstrates secure communication using hybrid encryption.
