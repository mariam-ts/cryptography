from week6.constants import BLOCK_SIZE


def split_blocks(data: bytes, block_size: int = BLOCK_SIZE) -> list[bytes]:
    """Split data into blocks of the specified size."""
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]