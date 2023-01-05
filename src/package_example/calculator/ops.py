from package_example.utils.conversions import bytes_to_uint16


def addition(bytes1, bytes2):
    """Convert two two bytes to unsigned integers
    and sum them.
    Does not handle overflow.

    Args:
        bytes1 (bytes): Two bytes
        bytes2 (bytes): Two bytes

    Raises:
        ValueError: The number of bytes in the arguments
        is not 2

    Returns:
        np.uint16: _description_
    """
    if len(bytes1) != 2 or len(bytes2) != 2:
        raise ValueError("The number of bytes must be 2")
    return bytes_to_uint16(bytes1) + bytes_to_uint16(bytes2)
