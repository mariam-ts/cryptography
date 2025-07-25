from week6.blockSplitting import split_blocks
from week6.singleBlockDecription import decrypt_block


def padding_oracle_attack(ciphertext: bytes) -> bytes:
    """Perform the padding oracle attack on the entire ciphertext."""
    blocks = split_blocks(ciphertext)
    decrypted = bytearray()

    for i in range(1, len(blocks)):
        prev = blocks[i-1]
        curr = blocks[i]
        decrypted_block = decrypt_block(prev, curr)
        decrypted.extend(decrypted_block)

    return bytes(decrypted)