from matplotlib import pyplot as plt

from package_example.utils.conversions import bytes_to_uint16


def plot_sine_from_bytes(bytes):
    """Plot sine wave from given bytes.
    The bytes are part of array of 16-bit unsigned
    integers.

    Args:
        bytes (bytes): Bytes containing sine-wave values.
    """
    sine = bytes_to_uint16(bytes)
    plt.figure(figsize=(8, 5))
    plt.plot(sine)
    plt.show()
