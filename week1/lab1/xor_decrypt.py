# xor_decrypt.py
import base64

def xor_decrypt(base64_input, key):
    data = base64.b64decode(base64_input)
    key_bytes = key.encode()
    decrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])
    return decrypted.decode(errors="ignore")

if __name__ == "__main__":
    ciphertext_b64 = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
    key = "secure"  # passphrase recovered from Caesar + anagram
    print("Decrypted message:", xor_decrypt(ciphertext_b64, key))


# Step 1:** Decrypt the Caesar-encrypted word `mznxpz` → `rescue`

# Step 2:** Solve the anagram → `secure`

# Step 3:** Use "secure" to XOR-decrypt the given base64 ciphertext

# final output: 'Decrypted message: This is the XOR challenge!'
