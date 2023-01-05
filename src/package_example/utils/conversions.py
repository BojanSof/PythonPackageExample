import numpy as np


def bytes_to_uint16(bytes):
    """Convert bytes to array of unsigned integer.
    Little endian is used.

    Args:
        bytes (bytes): Multiple bytes.

    Returns:
        np.ndarray: Array of integers obtained from the bytes.
    """
    return np.frombuffer(bytes, dtype=np.uint16)
