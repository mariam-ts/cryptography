from binascii import unhexlify
from week6.constants import BLOCK_SIZE, CIPHERTEXT_HEX
from week6.fullAttack import padding_oracle_attack
from week6.plainTextDecoding import unpad_and_decode


if __name__ == "__main__":
    try:
        ciphertext = unhexlify(CIPHERTEXT_HEX)
        print(f"[*] Ciphertext length: {len(ciphertext)} bytes")
        print(f"[*] IV: {ciphertext[:BLOCK_SIZE].hex()}")
        
        recovered = padding_oracle_attack(ciphertext)
        
        print("\n[+] Decryption complete!")
        print(f" Recovered plaintext (raw bytes): {recovered}")
        print(f" Hex: {recovered.hex()}")
        
        decoded = unpad_and_decode(recovered)
        print("\n Final plaintext:")
        print(decoded)
        
    except Exception as e:
        print(f"\n Error occurred: {e}")


# Decryption happens one byte at a time from the end of a block toward the beginning.

# Implementing padding oracle attacks requires patience, as guessing 256 values for each byte can be slow.

# Understanding the XOR relationships and how CBC mode propagates changes was key.