from week6.constants import BLOCK_SIZE
from cryptography.hazmat.primitives import padding

def decrypt_block(prev_block: bytes, target_block: bytes) -> bytes:
    """Decrypt a single block using the padding oracle attack."""
    intermediate = [0] * BLOCK_SIZE
    plaintext = bytearray(BLOCK_SIZE)

    for i in range(1, BLOCK_SIZE + 1):
        pad_byte = i
        prefix = bytearray(BLOCK_SIZE)

        for guess in range(256):
            for j in range(1, i):
                prefix[-j] = intermediate[-j] ^ pad_byte
            prefix[-i] = guess

            test_block = bytes(prefix) + target_block
            if padding_oracle(test_block):
                intermediate[-i] = guess ^ pad_byte
                plaintext[-i] = intermediate[-i] ^ prev_block[-i]
                break

    return bytes(plaintext)
