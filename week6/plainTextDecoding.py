from week6.constants import BLOCK_SIZE
from cryptography.hazmat.primitives import padding


def unpad_and_decode(plaintext: bytes) -> str:
    """Attempt to unpad and decode the plaintext."""
    unpadder = padding.PKCS7(BLOCK_SIZE * 8).unpadder()
    unpadded = unpadder.update(plaintext) + unpadder.finalize()
    return unpadded.decode('utf-8')
