import numpy as np


def bytes_to_uint16(bytes):
    """Convert two bytes to unsigned integer.
    Little endian is used.

    Args:
        bytes (bytes): Two bytes.

    Returns:
        np.uint16: The bytes converted to integer.
    """
    if len(bytes) != 2:
        raise ValueError("The number of bytes must be 2")
    return np.frombuffer(bytes, dtype=np.uint16)
